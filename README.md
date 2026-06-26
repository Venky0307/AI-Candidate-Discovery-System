# 🤖 AI Candidate Discovery System

An AI-powered Intelligent Candidate Discovery and Ranking System developed for the **India Runs Data & AI Challenge**.

The system leverages **semantic embeddings**, **feature engineering**, and a **hybrid ranking algorithm** to identify and rank the most relevant candidates for a given job description.

---

# 🚀 Features

* Semantic Job–Candidate Matching using Sentence Transformers
* Hybrid Candidate Ranking
* Intelligent Feature Engineering
* Explainable Candidate Recommendations
* Top-100 Candidate Selection
* Challenge-Compliant Submission Generation
* Streamlit Web Application

---

# 🏗️ System Workflow

```
Candidate Dataset (JSONL)
          │
          ▼
Data Loading & Preprocessing
          │
          ▼
Feature Engineering
          │
          ▼
Sentence Transformer Embeddings
          │
          ▼
Semantic Similarity Computation
          │
          ▼
Hybrid Ranking Engine
          │
          ▼
Top 100 Candidates
          │
          ▼
submission.csv
```

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Sentence Transformers
* Scikit-learn
* PyTorch
* Streamlit
* python-docx

---

# 📁 Project Structure

```
AI-Candidate-Discovery-System
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── embeddings.py
│   ├── feature_engineering.py
│   ├── preprocess.py
│   ├── rank_candidates.py
│   ├── submission.py
│   └── utils.py
│
├── models/
│
├── output/
│
├── app.py
├── requirements.txt
├── validate_submission.py
└── README.md
```

---

# 📊 Candidate Ranking Features

The ranking model considers multiple signals:

* Semantic similarity between candidate profile and job description
* Skills
* Years of experience
* Education
* Career history
* GitHub activity
* Profile completeness
* AI assessment scores
* Recruiter response rate
* Interview completion rate
* Offer acceptance rate
* Notice period
* Open-to-work status

These features are combined using a weighted hybrid ranking model to produce the final ranking score.

---

# 📂 Dataset

This project uses the **India Runs Data & AI Challenge** dataset.

Due to GitHub's file size limitations, the following files are **not included** in this repository:

| File                            | Description                          |
| ------------------------------- | ------------------------------------ |
| candidates.jsonl                | Original candidate dataset (~487 MB) |
| models/candidate_embeddings.npy | Generated semantic embeddings        |
| output/candidates_processed.csv | Generated preprocessing output       |
| output/ranked_candidates.csv    | Generated ranking output             |

These files can be regenerated using the provided scripts.

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Venky0307/AI-Candidate-Discovery-System.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Generate candidate embeddings

```bash
python test_embeddings.py
```

Rank candidates

```bash
python test_ranker.py
```

Generate the final submission

```bash
python test_submission.py
```

Validate the submission

```bash
python validate_submission.py output/submission.csv
```

Launch the web application

```bash
streamlit run app.py
```

---

# 📄 Output

The system generates:

* Candidate embeddings
* Ranked candidate list
* Explainable ranking
* Final challenge submission (`submission.csv`)

---

# 🔮 Future Improvements

* Cross-Encoder reranking
* LLM-based reasoning generation
* Resume PDF parsing
* FAISS vector database integration
* Recruiter dashboard with analytics
* Multi-job candidate recommendation
* Real-time candidate search

---

# 👨‍💻 Author

**Venkatesh Danda**

Developed as part of the **India Runs Data & AI Challenge**.

---
