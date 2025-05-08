import re

def analyze_resume(resume_text, keywords):
    resume_text = resume_text.lower()
    found_keywords = []

    for kw in keywords:
        pattern = r"\b" + re.escape(kw.lower()) + r"\b"
        if re.search(pattern, resume_text):
            found_keywords.append(kw)

    score = int((len(found_keywords) / len(keywords)) * 100) if keywords else 0
    return score, found_keywords
