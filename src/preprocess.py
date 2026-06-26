import json
import os
import pandas as pd
from typing import List, Dict


class CandidatePreprocessor:
    def __init__(self, jsonl_path):
        self.jsonl_path = jsonl_path

    def load_jsonl(self) -> List[Dict]:
        candidates = []

        with open(self.jsonl_path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    candidates.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

        return candidates

    def _extract_text(self, value):
        if value is None:
            return ""

        if isinstance(value, str):
            return value

        if isinstance(value, list):
            texts = []
            for item in value:
                if isinstance(item, dict):
                    texts.extend(str(v) for v in item.values())
                else:
                    texts.append(str(item))
            return " ".join(texts)

        if isinstance(value, dict):
            return " ".join(str(v) for v in value.values())

        return str(value)

    def flatten_candidates(self, candidates):

        rows = []

        for candidate in candidates:

            profile = candidate.get("profile", {})
            signals = candidate.get("redrob_signals", {})

            skills = candidate.get("skills", [])
            education = candidate.get("education", [])
            career = candidate.get("career_history", [])
            certifications = candidate.get("certifications", [])
            languages = candidate.get("languages", [])

            row = {}

            row["candidate_id"] = candidate.get("candidate_id", "")

            row["headline"] = profile.get("headline", "")
            row["summary"] = profile.get("summary", "")
            row["location"] = profile.get("location", "")
            row["country"] = profile.get("country", "")
            row["current_title"] = profile.get("current_title", "")
            row["current_company"] = profile.get("current_company", "")
            row["industry"] = profile.get("current_industry", "")
            row["years_of_experience"] = profile.get("years_of_experience", 0)

            row["skills"] = ", ".join(
                s.get("name", "") for s in skills
            )

            row["skill_count"] = len(skills)

            row["career_text"] = " ".join(
                f"{job.get('title','')} {job.get('description','')}"
                for job in career
            )

            row["education"] = " ".join(
                f"{e.get('degree','')} {e.get('field_of_study','')}"
                for e in education
            )

            row["certifications"] = ", ".join(
                c.get("name", str(c))
                if isinstance(c, dict)
                else str(c)
                for c in certifications
            )

            row["languages"] = ", ".join(
                l.get("language","")
                for l in languages
            )

            row["github_score"] = signals.get(
                "github_activity_score", 0
            )

            row["profile_score"] = signals.get(
                "profile_completeness_score", 0
            )

            row["notice_period"] = signals.get(
                "notice_period_days", 0
            )

            row["open_to_work"] = signals.get(
                "open_to_work_flag", False
            )

            rows.append(row)

        return pd.DataFrame(rows)

    def save_dataframe(self, df, output_path):

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        df.to_csv(output_path, index=False)

        print(f"\nSaved to: {output_path}")

    def dataset_summary(self, df):

        print("=" * 60)
        print("DATASET SUMMARY")
        print("=" * 60)

        print(f"Total Candidates : {len(df)}")
        print(f"Columns          : {len(df.columns)}")

        print("\nColumns:")
        for col in df.columns:
            print(f" - {col}")

        print("\nMissing Values:")

        print(df.isnull().sum())

        print("\nSample Candidate:")

        print(df.iloc[0])


def main():

    dataset_path = "candidates.jsonl"

    processor = CandidatePreprocessor(dataset_path)

    candidates = processor.load_jsonl()

    print(f"Loaded {len(candidates)} candidates")

    df = processor.flatten_candidates(candidates)

    processor.dataset_summary(df)

    processor.save_dataframe(
        df,
        "output/candidates_processed.csv"
    )


if __name__ == "__main__":
    main()