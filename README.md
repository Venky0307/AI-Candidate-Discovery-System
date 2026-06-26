# AI Candidate Discovery System

## Overview

An AI-powered recruitment system built for the India Runs Data & AI Challenge.

The system ranks candidates by combining:

- Semantic Search (Sentence Transformers)
- Skills Matching
- Experience Scoring
- Education Matching
- GitHub Activity
- Profile Completeness

## Tech Stack

- Python
- Sentence Transformers
- PyTorch
- Pandas
- Scikit-learn
- Streamlit

## Project Structure

```
src/
├── config.py
├── data_loader.py
├── preprocess.py
├── embeddings.py
├── feature_engineering.py
├── rank_candidates.py
├── submission.py
├── utils.py
```

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate embeddings:

```bash
python test_embeddings.py
```

Generate rankings:

```bash
python test_ranker.py
```

Run the application:

```bash
streamlit run app.py
```

## Output

- Ranked Candidates
- Submission CSV
- Recruiter Dashboard
