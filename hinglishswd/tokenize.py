import re
from hinglishswd.detect import detect_language

HINGLISH_PATTERNS = [
    (r"\b(?:nahi|na|mat)\b", " negation"),
    (r"\b(?:hai|hain|ho|hu|tha|the|thi|thay)\b", " be"),
    (r"\b(?:raha|rahi|rahe)\b", " prog"),
    (r"\b(?:sakta|sakti|sakte)\b", " can"),
    (r"\b(?:karta|karti|karte|karna)\b", " do"),
    (r"\b(?:chahiye|padega|hoga)\b", " modal"),
    (r"\b(?:wala|wali|wale)\b", " future"),
]

def tokenize(text, lang=None):
    text = str(text).strip().lower()
    if not text:
        return []
    if lang is None:
        lang = detect_language(text)
    if lang == "english":
        return text.split()
    if lang == "hindi":
        import spacy
        from spacy.lang.hi import Hindi
        nlp = Hindi()
        doc = nlp(text)
        return [token.text for token in doc]
    tokens = text.split()
    result = []
    for token in tokens:
        splits = re.split(r"([?.!,:;\-\"\'()\[\]{}<>/\\@#$%^&*_~`+=])", token)
        for part in splits:
            part = part.strip()
            if part:
                result.append(part)
    return result

def tokenize_sentences(text):
    text = str(text).strip()
    if not text:
        return []
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in sentences if s.strip()]
