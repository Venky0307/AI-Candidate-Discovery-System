import re
from docx import Document


def read_job_description(doc_path: str) -> str:
    """
    Read all text from a DOCX file.
    """
    document = Document(doc_path)

    paragraphs = []

    for para in document.paragraphs:
        text = para.text.strip()

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)


def clean_text(text: str) -> str:
    """
    Basic text cleaning.
    """
    if text is None:
        return ""

    text = text.lower()

    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\t", " ", text)
    text = re.sub(r"\s+", " ", text)

    text = re.sub(r"[^a-z0-9+#./ ]", " ", text)

    return text.strip()


def extract_keywords(text: str):

    stop_words = {
        "the","is","are","was","were","and","or","to","for",
        "of","in","on","at","with","as","an","a","be","by",
        "from","that","this","it","will","can","should","have"
    }

    words = clean_text(text).split()

    keywords = [
        word
        for word in words
        if len(word) > 2 and word not in stop_words
    ]

    return sorted(set(keywords))


def build_candidate_text(row):
    """
    Create one large document representing the candidate.
    """

    sections = [

        row.get("headline",""),

        row.get("summary",""),

        row.get("current_title",""),

        row.get("industry",""),

        row.get("skills",""),

        row.get("career_text",""),

        row.get("education",""),

        row.get("languages","")
    ]

    return clean_text(" ".join(str(s) for s in sections))