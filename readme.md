# 🌟 Vibe Matcher Prototype: Next-Generation Recommendation System for Nexora

## 🎯 Project Goal
To prototype a "Vibe Matcher" recommendation system that uses **OpenAI Embeddings** and **Cosine Similarity (sklearn)** to semantically match a user's free-text "vibe query" (e.g., "energetic urban chic") to the top products in a mock catalog.

## 📄 Deliverables
1.  **Code & Repository:** This GitHub repository contains all the code.
2.  **Notebook/Report:** The `notebooks/VibeMatcher_Report.ipynb` file (or a link to the Colab version) contains the run logs, latency plot, and detailed step-by-step execution.
3.  **Reflection:** The `REFLECTION.md` file contains the required reflection and suggested improvements (including Pinecone integration).

## 🚀 Quickstart Guide

### Prerequisites
* Python 3.8+
* An OpenAI API Key (Set as an environment variable)

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YourUsername/Vibe-Matcher-Nexora.git](https://github.com/YourUsername/Vibe-Matcher-Nexora.git)
    cd Vibe-Matcher-Nexora
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # .\venv\Scripts\activate # On Windows
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Set your OpenAI API key (replace `YOUR_API_KEY`):
    ```bash
    export OPENAI_API_KEY="YOUR_API_KEY"
    ```

### Run the Vibe Matcher
Execute the main script to run the defined test queries and see the output:
```bash
python run_matcher.py