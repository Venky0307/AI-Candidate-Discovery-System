"""
Hybrid Candidate Ranking Engine
"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from src.config import (
    WEIGHTS,
    TOP_K,
    RANKED_FILE
)

from src.embeddings import EmbeddingEngine
from src.feature_engineering import FeatureEngineer


class CandidateRanker:

    def __init__(self):

        self.embedding_engine = EmbeddingEngine()
        self.feature_engine = FeatureEngineer()

    def rank(self, dataframe, job_description):

        print("Loading candidate embeddings...")

        embeddings, ids = self.embedding_engine.load_embeddings()

        print("Embedding Job Description...")

        job_embedding = self.embedding_engine.embed_text(
            job_description
        )

        semantic_scores = cosine_similarity(
            [job_embedding],
            embeddings
        )[0]

        final_scores = []

        semantic_list = []
        skill_list = []
        experience_list = []
        education_list = []
        github_list = []
        profile_list = []
        assessment_list = []
        interview_list = []
        recruiter_list = []
        offer_list = []
        notice_list = []

        print("Calculating hybrid scores...")

        for idx, (_, row) in enumerate(dataframe.iterrows()):

            semantic = semantic_scores[idx]

            skill = self.feature_engine.skill_match_score(
                row["skills"],
                job_description
            )

            experience = self.feature_engine.experience_score(
                row["years_of_experience"]
            )

            education = self.feature_engine.education_score(
                row["education"]
            )

            github = self.feature_engine.github_score(
                row["github_score"]
            )

            profile = self.feature_engine.profile_score(
                row["profile_score"]
            )

            assessment = self.feature_engine.assessment_score(
                row["skill_assessment"]
            )

            interview = self.feature_engine.interview_score(
                row["interview_completion"]
            )

            recruiter = self.feature_engine.recruiter_score(
                row["recruiter_response"]
            )

            offer = self.feature_engine.offer_score(
                row["offer_acceptance"]
            )

            notice = self.feature_engine.notice_score(
                row["notice_period"]
            )

            score = (

                0.35 * semantic +

                0.15 * skill +

                0.10 * experience +

                0.05 * education +

                0.05 * github +

                0.05 * profile +

                0.10 * assessment +

                0.05 * interview +

                0.05 * recruiter +

                0.03 * offer +

                0.02 * notice

            )

            final_scores.append(score)

            semantic_list.append(semantic)
            skill_list.append(skill)
            experience_list.append(experience)
            education_list.append(education)
            github_list.append(github)
            profile_list.append(profile)
            assessment_list.append(assessment)
            interview_list.append(interview)
            recruiter_list.append(recruiter)
            offer_list.append(offer)
            notice_list.append(notice)

        dataframe = dataframe.copy()

        dataframe["semantic_score"] = semantic_list
        dataframe["skill_score"] = skill_list
        dataframe["experience_score"] = experience_list
        dataframe["education_score"] = education_list
        dataframe["github_score_norm"] = github_list
        dataframe["profile_score_norm"] = profile_list
        dataframe["assessment_score"] = assessment_list
        dataframe["interview_score"] = interview_list
        dataframe["recruiter_score"] = recruiter_list
        dataframe["offer_score"] = offer_list
        dataframe["notice_score"] = notice_list

        dataframe["final_score"] = final_scores

        dataframe = dataframe.sort_values(
            by="final_score",
            ascending=False
        )

        dataframe.to_csv(
            RANKED_FILE,
            index=False
        )

        print(f"Ranking saved to {RANKED_FILE}")

        return dataframe.head(TOP_K)