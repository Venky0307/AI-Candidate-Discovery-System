from src.data_loader import DataLoader
from src.embeddings import EmbeddingEngine

loader = DataLoader()

candidates = loader.load_candidates()

df = loader.candidates_to_dataframe(
    candidates
)

engine = EmbeddingEngine()

if not engine.embeddings_exist():

    embeddings = engine.embed_candidates(df)

else:

    embeddings, ids = engine.load_embeddings()

print(embeddings.shape)

print(embeddings[0][:10])