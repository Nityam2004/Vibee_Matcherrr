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

