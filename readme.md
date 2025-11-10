# 🌟 Nexora Vibe Matcher Prototype

### **A Semantic Product Recommendation System using Gemini Embeddings and Vector Search**

---

## 🧭 Overview

The **Nexora Vibe Matcher** is an intelligent semantic recommendation system that enhances product discovery by going beyond simple keyword matching. Instead, it captures the **semantic "vibe"** of user queries using **Google Gemini embeddings** and performs **vector-based similarity search** to recommend products that best align with user intent.

---

## 🚀 Key Features & Requirements

| Requirement | Status | Technology Used |
|--------------|---------|----------------|
| **Data Preparation** | ✅ Complete | Pandas DataFrame |
| **Embedding Generation** | ✅ Complete | Google `gemini-embedding-001` |
| **Vector Search** | ✅ Complete | `sklearn.metrics.pairwise.cosine_similarity` |
| **Top-K Output** | ✅ Complete | Outputs Top 3 ranked products with scores |
| **Edge Case Handling** | ✅ Implemented | Fallback prompt for `Score < 0.7` |
| **Testing / Evaluation** | ✅ Complete | Latency logging (`timeit`) and metrics saved |
| **Deliverables** | ✅ Prepared | Final reflection and reports saved |

---
---
## 🗂️ Project Structure


```bash
Vibe-Matcher-Nexora/
├── .gitignore               # Ignores venv and secret files
├── README.md                # This file
├── requirements.txt         # Project dependencies
├── run_matcher.py           # Main execution, testing, and logging script
├── src/
│   ├── __init__.py
│   └── vibe_match.py        # Core logic: Embedding functions & Vibe Matcher
├── data/
│   └── products.json        # Mock product catalog (7 items)
├── notebooks/
│   ├── latency_plot.png     # Saved visualization of performance
│   ├── latency_data.csv     # Raw performance data
│   └── log_metrics.csv      # Raw similarity scores and test results
└── REFLECTION.md            # Final submission: Detailed analysis and innovation

---

---

## ⚙️ Getting Started

### **Prerequisites**

- Python 3.8+
- A valid **Google Gemini API Key**

---

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/YourUsername/Nexora-Vibe-Matcher.git
cd Nexora-Vibe-Matcher
---
2️⃣ Setup Virtual Environment (Recommended)

macOS/Linux (or Git Bash):

python -m venv venv
source venv/bin/activate


Windows PowerShell:

python -m venv venv
.\venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Your API Key

⚠️ The Python Gemini client automatically reads your key from the GOOGLE_API_KEY environment variable.

PowerShell:

$env:GOOGLE_API_KEY="AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


Git Bash / macOS:

export GOOGLE_API_KEY="AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

5️⃣ Run the Vibe Matcher

Execute the main script to:

Generate embeddings

Perform vector search

Execute test queries

Log metrics and latency

python run_matcher.py

📊 Evaluation Output

Upon successful execution, the system prints a summary log table showing similarity metrics and top recommendations.

All output files are stored in the notebooks/ directory:

File	Description
latency_plot.png	Visualization of response time per query
log_metrics.csv	Raw similarity scores and threshold check (Score > 0.7)
latency_data.csv	Raw performance data with latency measurements
🧠 How It Works
Embedding Generation

Product descriptions and user queries are converted into numerical vectors using Gemini Embeddings.

Vector Search

Cosine Similarity compares embeddings to determine how semantically similar each product is to the user’s query.

Top-K Ranking

Products are ranked, and the top 3 with the highest similarity scores are returned.

Edge Case Handling

If no score exceeds 0.7, the system triggers a fallback message prompting the user for more details.

🔬 Example Output

Input Query:

"Cozy cotton hoodie for winter"

Top 3 Results:

Rank	Product Name	Similarity Score
1️⃣	Soft Cotton Hoodie	0.93
2️⃣	Winter Comfort Pullover	0.88
3️⃣	Thermal Sweatshirt	0.85

✅ All above 0.7 threshold — no fallback triggered.

📈 Performance Metrics

Average Embedding Generation Time: 0.25 s/query

Average Vector Search Time: 0.03 s/query

Overall Latency: ~0.28 s/query

Similarity Threshold: 0.7

Performance graphs are visualized in notebooks/latency_plot.png.

🧩 Future Enhancements

🔹 Integration with Pinecone or FAISS for large-scale vector databases

🔹 Add UI layer using Streamlit for real-time user interaction

🔹 Dynamic threshold optimization based on query complexity

🔹 Expand dataset and integrate real product metadata

🪄 Example Code Snippet
from src.vibe_match import VibeMatcher

matcher = VibeMatcher(data_path="data/products.json")
query = "eco-friendly bamboo sunglasses"

top_products = matcher.match(query, top_k=3)
for i, (product, score) in enumerate(top_products):
    print(f"{i+1}. {product['name']} — Score: {score:.2f}")

📚 References

Google AI Studio: Gemini Embeddings API

scikit-learn cosine_similarity Documentation

Pandas Official Docs

Python timeit Module

🧾 Author

Developed by: Nityam Rajput

Project: Nexora Semantic Vibe Matcher
License: MIT License © 2025

“Find not just what matches your words — but what matches your vibe.”

