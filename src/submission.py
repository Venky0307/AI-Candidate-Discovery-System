"""
Generate submission.csv
"""

import pandas as pd

from src.config import (
    RANKED_FILE,
    SUBMISSION_FILE
)


class SubmissionGenerator:

    def __init__(self):
        pass

    def generate_reasoning(self, row):

        reasons = []

        reasons.append(
            f"{row['headline']}"
        )

        reasons.append(
            f"{row['years_of_experience']:.1f} yrs experience"
        )

        if row["skill_count"] > 0:
            reasons.append(
                f"{int(row['skill_count'])} skills"
            )

        if row["github_score"] >= 7:
            reasons.append(
                f"GitHub {row['github_score']:.1f}/10"
            )

        if row["assessment_score"] >= 0.6:
            reasons.append(
                "Strong AI assessment"
            )

        if row["open_to_work"]:
            reasons.append(
                "Open to work"
            )

        if row["notice_period"] <= 30:
            reasons.append(
                "Available within 30 days"
            )

        return "; ".join(reasons)

    def generate_submission(self):

        df = pd.read_csv(RANKED_FILE)
        df = df.head(100).copy()

        df = df.sort_values(
            by=["final_score", "candidate_id"],
            ascending=[False, True]
        ).reset_index(drop=True)

        # Normalize score
        df["score"] = (
            df["final_score"] - df["final_score"].min()
        ) / (
            df["final_score"].max() - df["final_score"].min()
        )

        df["score"] = df["score"].round(3)

        df["rank"] = range(1, 101)

        df["reasoning"] = df.apply(
            self.generate_reasoning,
            axis=1
        )

        submission = df[
            [
                "candidate_id",
                "rank",
                "score",
                "reasoning"
            ]
        ]

        submission.to_csv(
            SUBMISSION_FILE,
            index=False
        )

        print(f"Submission saved to {SUBMISSION_FILE}")

        return submission