"""
Generate and cache embeddings for candidates and job descriptions.
"""

import os
import pickle
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

from src.config import (
    EMBEDDING_MODEL,
    EMBEDDINGS_FILE,
    CANDIDATE_IDS_FILE,
    BATCH_SIZE
)

from src.utils import build_candidate_text


class EmbeddingEngine:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        print("Model loaded successfully!")

    def embed_text(self, text):

        return self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def embed_candidates(self, dataframe):

        texts = []

        ids = []

        for _, row in dataframe.iterrows():

            texts.append(
                build_candidate_text(row)
            )

            ids.append(
                row["candidate_id"]
            )

        print(f"Generating embeddings for {len(texts):,} candidates...")

        embeddings = self.model.encode(

            texts,

            batch_size=BATCH_SIZE,

            show_progress_bar=True,

            convert_to_numpy=True,

            normalize_embeddings=True

        )

        np.save(
            EMBEDDINGS_FILE,
            embeddings
        )

        with open(
            CANDIDATE_IDS_FILE,
            "wb"
        ) as f:

            pickle.dump(ids, f)

        print("Embeddings saved.")

        return embeddings

    def load_embeddings(self):

        embeddings = np.load(
            EMBEDDINGS_FILE
        )

        with open(
            CANDIDATE_IDS_FILE,
            "rb"
        ) as f:

            ids = pickle.load(f)

        return embeddings, ids

    def embeddings_exist(self):

        return (

            os.path.exists(EMBEDDINGS_FILE)

            and

            os.path.exists(CANDIDATE_IDS_FILE)

        )