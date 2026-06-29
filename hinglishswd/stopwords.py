STOPWORDS_HINDI = {
    "ka", "ki", "ke", "ko", "se", "mein", "par", "aur", "yeh", "woh",
    "hai", "hain", "ho", "hu", "tha", "the", "thi", "thay", "kya", "kyun",
    "kaise", "kab", "kahan", "ye", "vo", "is", "us", "in", "un", "unka",
    "inka", "unki", "mera", "tera", "apna", "kuch", "bahut", "thoda",
    "abhi", "ab", "phir", "fir", "tab", "jab", "aap", "tum", "main",
    "hum", "mujhe", "tujhe", "humein", "unhe", "unko", "inke", "unke",
    "karo", "karein", "kar", "karta", "karti", "karte", "karna", "hota",
    "hoti", "hote", "raha", "rahi", "rahe", "chuka", "chuki", "chuke",
    "sakta", "sakti", "sakte", "diya", "liya", "liye", "lena",
    "dena", "hua", "hui", "hue", "gaya", "gayi", "gaye", "sab", "saare",
    "kisi", "kisiko", "kuchh", "jis", "jisko", "jinka", "jinki", "jinke",
}

STOPWORDS_HINGLISH = {
    "ka", "ki", "ke", "ko", "se", "mein", "par", "aur", "yeh", "woh",
    "hai", "hain", "ho", "hu", "tha", "the", "thi", "kya", "kyun",
    "kaise", "kab", "kahan", "ye", "vo", "is", "us", "in", "un",
    "mera", "tera", "apna", "kuch", "bahut", "thoda",
    "abhi", "ab", "phir", "fir", "tab", "jab", "aap", "tum", "main",
    "hum", "mujhe", "tujhe", "humein", "unhe", "unko",
    "karo", "karein", "kar", "karta", "karti", "karte", "karna", "hota",
    "hoti", "hote", "raha", "rahi", "rahe",
    "sakta", "sakti", "sakte", "diya", "liya", "liye", "lena",
    "dena", "hua", "hui", "hue", "gaya", "gayi", "gaye", "sab",
    "kisi", "kuchh", "jis",
    "hmm", "haan", "nahi", "acha", "achha", "theek", "thik",
    "ok", "okay", "bye", "hello", "namaste", "ji",
    "bank", "account", "customer", "rm", "sir", "madam",
    "really", "just", "also", "well", "get", "got",
}

def remove_stopwords(tokens, lang="hinglish"):
    stopwords = STOPWORDS_HINGLISH if lang == "hinglish" else STOPWORDS_HINDI
    return [t for t in tokens if t.lower() not in stopwords]
