from src.submission import SubmissionGenerator

generator = SubmissionGenerator()

submission = generator.generate_submission()

print(submission.head())