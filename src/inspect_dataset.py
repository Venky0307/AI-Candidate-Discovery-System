import json
from pprint import pprint
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

dataset_path = os.path.join(PROJECT_DIR, "candidates.jsonl")

with open(dataset_path, "r", encoding="utf-8") as f:
    first = json.loads(next(f))

print("=" * 100)
pprint(first)