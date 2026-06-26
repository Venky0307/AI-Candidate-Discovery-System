from src.data_loader import DataLoader
from src.rank_candidates import CandidateRanker

loader = DataLoader()

candidates = loader.load_candidates()

df = loader.candidates_to_dataframe(candidates)

job = loader.load_job_description()

ranker = CandidateRanker()

top = ranker.rank(df, job)

print(top[[
    "candidate_id",
    "headline",
    "years_of_experience",
    "final_score"
]])