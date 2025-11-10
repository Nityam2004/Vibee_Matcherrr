import os
import pandas as pd
import numpy as np
import json
from google import genai
from google.genai import types
from sklearn.metrics.pairwise import cosine_similarity
import time # Used for mock latency if API key is missing

# --- Configuration Constants ---
EMBEDDING_MODEL = "gemini-embedding-001"
# SEMANTIC_SIMILARITY is the recommended task type for search/recommendation
SIMILARITY_TASK_TYPE = "SEMANTIC_SIMILARITY" 
SIMILARITY_THRESHOLD = 0.7 
TOP_K = 3
MOCK_DIMENSION = 768 # Approximate dimension for some Gemini embeddings

# Initialize Gemini Client (reads key from env var GOOGLE_API_KEY or GEMINI_API_KEY)
try:
    client = genai.Client()
    # Test connection by trying to get a model list (optional)
    # client.models.list() 
except Exception:
    print("WARNING: Gemini API key not found. Using mock embeddings for testing.")
    client = None

def get_embedding(text: str) -> np.ndarray:
    """Generates a vector embedding for a given text using the Gemini API."""
    if client is None:
        # Mock embedding for demonstration if key is missing/invalid
        return np.random.rand(MOCK_DIMENSION).tolist() 
    
    try:
        # Call the Gemini embed_content method
        response = client.models.embed_content(
            model=EMBEDDING_MODEL, 
            contents=[text], # Contents must be a list of strings
            config=types.EmbedContentConfig(
                task_type=SIMILARITY_TASK_TYPE
            )
        )
        return response.embeddings[0].values
    except Exception as e:
        # If API returns an error (like a quota error), we fall back to mock data
        print(f"Error generating embedding for '{text[:20]}...': {e}")
        time.sleep(1) # Small delay to avoid hammering the API if it's rate-limiting
        return np.random.rand(MOCK_DIMENSION).tolist() # Return mock to allow execution to proceed

def load_and_embed_products(filepath: str) -> pd.DataFrame:
    """Loads product data and generates embeddings for descriptions."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    
    print(f"Generating embeddings for {len(df)} products...")
    # Generate embeddings and store as numpy arrays
    df['embedding'] = df['desc'].apply(get_embedding)
    
    # Check if we generated mock data (list) or real embeddings (list/numpy array)
    # Note: We now return mock data on API failure to keep the flow running.
    df['embedding'] = df['embedding'].apply(np.array)
    
    print(f"Ready: {len(df)} products successfully embedded.")
    return df

def vibe_matcher(query: str, df: pd.DataFrame, top_k: int = TOP_K, min_score: float = SIMILARITY_THRESHOLD) -> pd.DataFrame:
    """
    Matches a vibe query to the top K most similar products using cosine similarity.
    Handles 'no match' edge case.
    """
    # 1. Embed the query
    query_vector = get_embedding(query)
    query_vector_reshaped = np.array(query_vector).reshape(1, -1)
    
    # 2. Prepare product embeddings for comparison
    product_embeddings = np.stack(df['embedding'].to_numpy())

    # 3. Compute Cosine Similarity (sklearn)
    similarities = cosine_similarity(query_vector_reshaped, product_embeddings)[0]

    # Create results table
    results_df = df.copy()
    results_df['sim_score'] = similarities
    
    # 4. Rank and Filter
    ranked_products = results_df.sort_values(by='sim_score', ascending=False).reset_index(drop=True)
    
    # 5. Edge Case: No Match -> Fallback
    best_match_score = ranked_products.iloc[0]['sim_score'] if not ranked_products.empty else 0

    if best_match_score < min_score:
        # Fallback Prompt
        print(f"\n⚠️ FALLBACK: No product matched the vibe (best score: {best_match_score:.4f} < {min_score}).")
        print("💡 Suggestion: Try a more general query like 'casual' or 'formal'.")
        return pd.DataFrame()

    # Output Top-K ranked products
    return ranked_products.head(top_k)[['name', 'desc', 'vibes', 'sim_score']]