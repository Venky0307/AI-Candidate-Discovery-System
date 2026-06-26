from src.data_loader import DataLoader

loader = DataLoader()

candidates = loader.load_candidates()

print(candidates[0].keys())

df = loader.candidates_to_dataframe(candidates)

print(df.head())

print(df.shape)

job = loader.load_job_description()

print(job[:500])