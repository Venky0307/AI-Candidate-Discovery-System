"""
Feature Engineering Module
"""

import re


class FeatureEngineer:

    # -------------------------------
    # Semantic Skill Match
    # -------------------------------

    def skill_match_score(self, candidate_skills, job_description):

        if not candidate_skills:
            return 0.0

        candidate = {
            s.strip().lower()
            for s in candidate_skills.split(",")
            if s.strip()
        }

        job = {
            s.lower()
            for s in re.findall(
                r"[A-Za-z0-9+#.]+",
                job_description
            )
        }

        if len(candidate) == 0:
            return 0.0

        overlap = candidate.intersection(job)

        return len(overlap) / len(candidate)

    # -------------------------------
    # Experience
    # -------------------------------

    def experience_score(self, years):

        if years >= 8:
            return 1.0

        if years >= 5:
            return 0.8

        if years >= 3:
            return 0.6

        return years / 5

    # -------------------------------
    # Education
    # -------------------------------

    def education_score(self, education):

        education = str(education).lower()

        if "phd" in education:
            return 1.0

        if "m.tech" in education or "master" in education:
            return 0.9

        if "b.tech" in education or "b.e" in education:
            return 0.8

        return 0.6

    # -------------------------------
    # Tier
    # -------------------------------

    def education_tier_score(self, tier):

        tier = str(tier).lower()

        if "tier_1" in tier:
            return 1.0

        if "tier_2" in tier:
            return 0.8

        if "tier_3" in tier:
            return 0.6

        return 0.5

    # -------------------------------
    # GitHub
    # -------------------------------

    def github_score(self, score):

        return min(score / 10, 1.0)

    # -------------------------------
    # Profile Completeness
    # -------------------------------

    def profile_score(self, score):

        return min(score / 100, 1.0)

    # -------------------------------
    # AI Assessment
    # -------------------------------

    def assessment_score(self, assessment):

        if not assessment:
            return 0

        values = list(assessment.values())

        return sum(values) / (100 * len(values))

    # -------------------------------
    # Endorsements
    # -------------------------------

    def endorsement_score(self, endorsements):

        return min(endorsements / 100, 1.0)

    # -------------------------------
    # Interview
    # -------------------------------

    def interview_score(self, score):

        return score

    # -------------------------------
    # Recruiter
    # -------------------------------

    def recruiter_score(self, score):

        return score

    # -------------------------------
    # Offer
    # -------------------------------

    def offer_score(self, score):

        return score

    # -------------------------------
    # Notice Period
    # -------------------------------

    def notice_score(self, days):

        if days <= 30:
            return 1.0

        if days <= 60:
            return 0.8

        return 0.5

    # -------------------------------
    # Open To Work
    # -------------------------------

    def open_to_work_score(self, flag):

        return 1.0 if flag else 0.4

    # -------------------------------
    # Relocation
    # -------------------------------

    def relocation_score(self, flag):

        return 1.0 if flag else 0.5

    # -------------------------------
    # Work Mode
    # -------------------------------

    def work_mode_score(self, mode):

        mode = str(mode).lower()

        if mode == "hybrid":
            return 1.0

        if mode == "onsite":
            return 0.9

        if mode == "remote":
            return 0.8

        return 0.5