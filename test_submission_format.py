import pandas as pd

df = pd.read_csv("sample_submission.csv")

print(df.head())

print("\nColumns:")
print(df.columns.tolist())