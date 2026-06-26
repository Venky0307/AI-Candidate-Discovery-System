"""
Project Configuration
"""

import os

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(BASE_DIR, "candidates.jsonl")

JOB_DESCRIPTION_PATH = os.path.join(
    BASE_DIR,
    "job_description.docx"
)

OUTPUT_DIR = os.path.join(BASE_DIR, "output")

MODEL_DIR = os.path.join(BASE_DIR, "models")

PROCESSED_DATA = os.path.join(
    OUTPUT_DIR,
    "candidates_processed.csv"
)

EMBEDDINGS_FILE = os.path.join(
    MODEL_DIR,
    "candidate_embeddings.npy"
)

CANDIDATE_IDS_FILE = os.path.join(
    MODEL_DIR,
    "candidate_ids.pkl"
)

SUBMISSION_FILE = os.path.join(
    OUTPUT_DIR,
    "submission.csv"
)

RANKED_FILE = os.path.join(
    OUTPUT_DIR,
    "ranked_candidates.csv"
)

# ==========================================================
# MODEL CONFIGURATION
# ==========================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

BATCH_SIZE = 128

TOP_K = 100

# ==========================================================
# HYBRID SCORING WEIGHTS
# ==========================================================

WEIGHTS = {
    "semantic": 0.35,
    "skills": 0.15,
    "experience": 0.10,
    "education": 0.05,
    "github": 0.05,
    "profile": 0.05,
    "assessment": 0.10,
    "interview": 0.05,
    "recruiter": 0.05,
    "offer": 0.03,
    "notice": 0.02,
}

# ==========================================================
# CREATE DIRECTORIES
# ==========================================================

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)