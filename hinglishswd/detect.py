import re

DEVANAGARI_START = 0x0900
DEVANAGARI_END = 0x097F

_HINGLISH_INDICATORS = {
    "hai", "hain", "ho", "hu", "tha", "the", "thi", "thay",
    "raha", "rahi", "rahe", "hoon", "hota", "hoti", "hote",
    "karta", "karti", "karte", "karna", "karo", "karein",
    "sakta", "sakti", "sakte", "chahiye", "padega",
    "ka", "ki", "ke", "ko", "se", "mein", "par", "aur",
    "mera", "tera", "apna", "hum", "tum", "aap", "mujhe", "tujhe",
    "nahi", "haan", "hmm", "acha", "achha", "theek", "thik",
    "bahut", "thoda", "kuch", "abhi", "phir", "fir",
    "wala", "wali", "wale", "gaya", "gayi", "gaye",
    "hua", "hui", "hue", "diya", "liya", "liye",
    "kya", "kyun", "kaise", "kab", "kahan", "kis",
    "namaste", "ji", "sir", "madam",
}

def detect_language(text):
    text = str(text).strip()
    if not text:
        return "unknown"
    devanagari_count = sum(1 for ch in text if DEVANAGARI_START <= ord(ch) <= DEVANAGARI_END)
    total = len(text)
    ratio = devanagari_count / total
    if ratio > 0.4:
        return "hindi"
    elif ratio > 0.05:
        return "hinglish"
    words = set(re.findall(r"[a-zA-Z]+", text.lower()))
    if words:
        hinglish_score = sum(1 for w in words if w in _HINGLISH_INDICATORS)
        if hinglish_score >= 2 or (hinglish_score == 1 and len(words) >= 3):
            return "hinglish"
    return "english"
