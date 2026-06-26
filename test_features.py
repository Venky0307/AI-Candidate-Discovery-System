from src.feature_engineering import FeatureEngineer

engine = FeatureEngineer()

print(
    engine.skill_match_score(
        "Python, NLP, AWS, Spark",
        "Need Python NLP Spark Engineer"
    )
)

print(
    engine.experience_score(6.9)
)

print(
    engine.github_score(8.2)
)

print(
    engine.profile_score(91)
)

print(
    engine.education_score(
        "B.Tech Computer Science"
    )
)

print(
    engine.career_score(
        "Built NLP and LLM pipelines using Spark",
        "Looking for LLM NLP Spark Engineer"
    )
)