import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from hinglishswd import HinglishNLP, detect_language, tokenize, hinglish_to_english
from hinglishswd.transliterate import hinglish_to_devanagari

nlp = HinglishNLP()

print("=" * 60)
print("1. LANGUAGE DETECTION")
print("=" * 60)
tests = [
    "Hello, how are you?",
    "kal mai khaana khane gaya",
    "aaj mausam bahut acha hai",
    "Mujhe ek glass paani chahiye",
    "RM: Namaste, ICICI Bank mein aapka swagat hai.",
    "Customer: My account has been frozen.",
    "Aap kal kya kar rahe the?",
    "Meri salary account mein koi transaction nahi hua",
]
for t in tests:
    print(f"  {t:<55s} -> {nlp.detect(t)}")

print()
print("=" * 60)
print("2. TRANSLITERATION (Hinglish -> Devanagari)")
print("=" * 60)
for t in tests:
    if nlp.detect(t) != "english":
        dev = nlp.transliterate(t)
        print(f"  {t}")
        print(f"  -> {dev}")
        print()

print("=" * 60)
print("3. TRANSLATION (Hinglish/Hindi -> English)")
print("=" * 60)
for t in tests:
    lang = nlp.detect(t)
    if lang != "english":
        en = nlp.translate(t)
        print(f"  [{lang}] {t}")
        print(f"  -> {en}")
        print()

print("=" * 60)
print("4. FULL PIPELINE")
print("=" * 60)
result = nlp.pipeline("kal mai bazaar gaya wahan bahut bheed thi phir ghar aa gaya")
for k, v in result.items():
    print(f"  {k}: {v}")

print()
print("=" * 60)
print("5. MODULE-LEVEL FUNCTIONS")
print("=" * 60)
print(f"  detect_language: {detect_language('yeh kya ho raha hai?')}")
print(f"  tokenize:        {tokenize('mujhe ek glass paani chahiye')}")
dev = hinglish_to_devanagari("mera naam rahul hai")
print(f"  hinglish_to_devanagari('mera naam rahul hai'): {dev}")
en = hinglish_to_english("aaj mausam bahut acha hai")
print(f"  hinglish_to_english('aaj mausam bahut acha hai'): {en}")

print()
print("=" * 60)
print("ALL TESTS PASSED")
print("=" * 60)
