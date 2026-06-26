import streamlit as st
import pandas as pd

from src.data_loader import DataLoader
from src.rank_candidates import CandidateRanker
from src.submission import SubmissionGenerator

st.set_page_config(
    page_title="AI Candidate Discovery",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Candidate Discovery System")
st.write("Rank candidates using Semantic Search + Hybrid AI Scoring")

loader = DataLoader()

job_description = loader.load_job_description()

with st.expander("📄 Job Description"):
    st.write(job_description)

if st.button("🚀 Rank Candidates"):

    with st.spinner("Loading candidates..."):

        candidates = loader.load_candidates()

        df = loader.candidates_to_dataframe(candidates)

    with st.spinner("Ranking candidates..."):

        ranker = CandidateRanker()

        top_candidates = ranker.rank(
            df,
            job_description
        )

    st.success("Ranking Complete!")

    st.subheader("🏆 Top Candidates")

    st.dataframe(
        top_candidates[
            [
                "candidate_id",
                "headline",
                "years_of_experience",
                "final_score"
            ]
        ],
        use_container_width=True
    )

    generator = SubmissionGenerator()

    submission = generator.generate_submission()

    st.subheader("Submission Preview")

    st.dataframe(
        submission.head(20),
        use_container_width=True
    )

    with open(
        "output/submission.csv",
        "rb"
    ) as f:

        st.download_button(
            label="📥 Download Submission",
            data=f,
            file_name="submission.csv",
            mime="text/csv"
        )