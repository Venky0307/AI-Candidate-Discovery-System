"""
Loads candidates dataset and job description.
"""

import json
import pandas as pd

from src.config import DATASET_PATH, JOB_DESCRIPTION_PATH
from src.utils import read_job_description


class DataLoader:

    def __init__(self):
        self.dataset_path = DATASET_PATH
        self.job_description_path = JOB_DESCRIPTION_PATH

    def load_candidates(self):
        """
        Load candidates from JSONL file.
        """

        candidates = []

        with open(self.dataset_path, "r", encoding="utf-8") as f:

            for line in f:

                try:
                    candidates.append(json.loads(line))

                except Exception:
                    continue

        print(f"Loaded {len(candidates):,} candidates")

        return candidates

    def load_job_description(self):
        """
        Load Job Description from DOCX.
        """

        return read_job_description(
            self.job_description_path
        )

    def candidates_to_dataframe(self, candidates):
        """
        Convert candidate JSON into a DataFrame.
        """

        rows = []

        for candidate in candidates:

            profile = candidate.get("profile", {})
            signals = candidate.get("redrob_signals", {})

            skills = candidate.get("skills", [])
            education = candidate.get("education", [])
            career = candidate.get("career_history", [])
            languages = candidate.get("languages", [])
            certifications = candidate.get("certifications", [])

            row = {

                # -------------------------------------------------
                # Basic Information
                # -------------------------------------------------

                "candidate_id": candidate.get("candidate_id", ""),

                "headline": profile.get("headline", ""),

                "summary": profile.get("summary", ""),

                "location": profile.get("location", ""),

                "country": profile.get("country", ""),

                "current_title": profile.get("current_title", ""),

                "current_company": profile.get("current_company", ""),

                "current_company_size": profile.get(
                    "current_company_size", ""
                ),

                "industry": profile.get(
                    "current_industry", ""
                ),

                "years_of_experience": profile.get(
                    "years_of_experience", 0
                ),

                # -------------------------------------------------
                # Skills
                # -------------------------------------------------

                "skills": ", ".join(
                    skill.get("name", "")
                    for skill in skills
                ),

                "skill_count": len(skills),

                "skill_proficiency": ", ".join(
                    skill.get("proficiency", "")
                    for skill in skills
                ),

                "skill_endorsements": sum(
                    skill.get("endorsements", 0)
                    for skill in skills
                ),

                "average_skill_duration": (
                    sum(
                        skill.get("duration_months", 0)
                        for skill in skills
                    ) / len(skills)
                    if skills else 0
                ),

                # -------------------------------------------------
                # Career
                # -------------------------------------------------

                "career_text": " ".join(
                    job.get("description", "")
                    for job in career
                ),

                "career_titles": ", ".join(
                    job.get("title", "")
                    for job in career
                ),

                "career_companies": ", ".join(
                    job.get("company", "")
                    for job in career
                ),

                "career_duration": sum(
                    job.get("duration_months", 0)
                    for job in career
                ),

                # -------------------------------------------------
                # Education
                # -------------------------------------------------

                "education": " ".join(
                    f"{edu.get('degree','')} "
                    f"{edu.get('field_of_study','')}"
                    for edu in education
                ),

                "education_tier": ", ".join(
                    edu.get("tier", "")
                    for edu in education
                ),

                "education_grade": ", ".join(
                    edu.get("grade", "")
                    for edu in education
                ),

                # -------------------------------------------------
                # Certifications
                # -------------------------------------------------

                "certification_count": len(certifications),

                # -------------------------------------------------
                # Languages
                # -------------------------------------------------

                "languages": ", ".join(
                    lang.get("language", "")
                    for lang in languages
                ),

                # -------------------------------------------------
                # Redrob Signals
                # -------------------------------------------------

                "github_score":
                    signals.get("github_activity_score", 0),

                "profile_score":
                    signals.get("profile_completeness_score", 0),

                "interview_completion":
                    signals.get("interview_completion_rate", 0),

                "offer_acceptance":
                    signals.get("offer_acceptance_rate", 0),

                "recruiter_response":
                    signals.get("recruiter_response_rate", 0),

                "notice_period":
                    signals.get("notice_period_days", 0),

                "open_to_work":
                    signals.get("open_to_work_flag", False),

                "preferred_work_mode":
                    signals.get("preferred_work_mode", ""),

                "willing_to_relocate":
                    signals.get("willing_to_relocate", False),

                "profile_views":
                    signals.get(
                        "profile_views_received_30d", 0
                    ),

                "applications":
                    signals.get(
                        "applications_submitted_30d", 0
                    ),

                "search_appearance":
                    signals.get(
                        "search_appearance_30d", 0
                    ),

                "saved_by_recruiters":
                    signals.get(
                        "saved_by_recruiters_30d", 0
                    ),

                "connection_count":
                    signals.get("connection_count", 0),

                "endorsements_received":
                    signals.get(
                        "endorsements_received", 0
                    ),

                "verified_email":
                    signals.get("verified_email", False),

                "verified_phone":
                    signals.get("verified_phone", False),

                "linkedin_connected":
                    signals.get(
                        "linkedin_connected", False
                    ),

                "last_active_date":
                    signals.get("last_active_date", ""),

                "salary_min":
                    signals.get(
                        "expected_salary_range_inr_lpa", {}
                    ).get("min", 0),

                "salary_max":
                    signals.get(
                        "expected_salary_range_inr_lpa", {}
                    ).get("max", 0),

                "skill_assessment":
                    signals.get(
                        "skill_assessment_scores", {}
                    ),
            }

            rows.append(row)

        df = pd.DataFrame(rows)

        return df