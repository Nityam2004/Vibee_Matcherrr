import pandas as pd
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import os
import json # Needed for saving reflection data
import sys

# Use the correct import location. Assumes src/vibe_match.py is present.
try:
    from src.vibe_match import load_and_embed_products, vibe_matcher, SIMILARITY_THRESHOLD
except ImportError:
    print("Error: Could not import core modules from src/vibe_match.py.")
    print("Please ensure src/vibe_match.py exists and dependencies are installed.")
    sys.exit(1)


def run_evaluation():
    # --- Data Prep & Embedding ---
    data_path = 'data/products.json'
    df_products = load_and_embed_products(data_path)

    # --- Setup Logs ---
    latency_log = []
    all_results = []
    
    # --- DEBUG/FLOW CONFIRMATION ---
    print("\n[DEBUG] Starting evaluation loop now...")
    # -------------------------------
    
    if df_products.empty or 'embedding' not in df_products.columns:
         print("Cannot run matcher without product embeddings. Exiting.")
         return

    # --- Test Queries & Evaluation Setup ---
    test_queries = [
        "energetic urban chic",
        "professional and sharp look",
        "something quiet and cozy for home",
        "extremely wild purple glitter party outfit with wings and horns", # Edge Case: No match expected
    ]

    print("\n" + "="*50)
    print("         STARTING VIBE MATCHER EVALUATION")
    print("="*50)

    for i, query in enumerate(test_queries):
        start_time = timer()
        
        # --- Vibe Matcher Execution ---
        results = vibe_matcher(query, df_products.copy()) 
        
        end_time = timer()
        latency = end_time - start_time
        latency_log.append({"query": query, "latency": latency})
        
        print(f"📊 Latency (timeit): {latency:.4f} seconds")

        if not results.empty:
            print(f"\n✅ TOP 3 RESULTS for '{query}':")
            for index, row in results.iterrows():
                match_status = "Good" if row['sim_score'] >= SIMILARITY_THRESHOLD else "Acceptable"
                
                # Log metrics
                log_entry = {
                    "query_id": i + 1,
                    "query": query,
                    "product": row['name'],
                    "sim_score": row['sim_score'],
                    "status": match_status
                }
                all_results.append(log_entry)
                print(f"    {index+1}. {row['name']} | Score: {row['sim_score']:.4f} ({match_status})")
        
        print("-" * 50)


    # =======================================================
    #                   ASSIGNMENT DELIVERABLES
    # =======================================================

    # --- 1. Latency Plot & Data (Test & Eval Requirement) ---
    print("\n--- GENERATING LATENCY REPORT ---")
    latency_df = pd.DataFrame(latency_log)
    
    plt.figure(figsize=(10, 5))
    plt.bar(latency_df['query'], latency_df['latency'], color='teal')
    plt.ylabel('Latency (Seconds)')
    plt.title('Vibe Matcher Query Latency')
    plt.xticks(rotation=15, ha='right')
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    
    # Save files for Notebook deliverable
    plt.savefig('notebooks/latency_plot.png') 
    latency_df.to_csv('notebooks/latency_data.csv', index=False)
    print("Latency plot and data saved to 'notebooks/' directory.")


    # --- 2. Final Log Metrics Table (Accuracy/Eval Requirement) ---
    print("\n--- FINAL LOG METRICS (Criteria: Sim Score > 0.7 = 'Good') ---")
    log_df = pd.DataFrame(all_results)
    
    if not log_df.empty:
        # Print Markdown table to console (for easy viewing)
        print(log_df.to_markdown(index=False)) 
        
        # Save metrics data to CSV for Notebook
        log_df.to_csv('notebooks/log_metrics.csv', index=False)
        print("Log metrics data saved to 'notebooks/log_metrics.csv'.")
    else:
        print("No successful matches (score > min_score) were logged.")


if __name__ == "__main__":
    # Ensure the directory for deliverables exists
    os.makedirs('notebooks', exist_ok=True)
    run_evaluation()