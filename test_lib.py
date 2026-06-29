import sys
sys.path.insert(0, '.')
from hinglishswd import HinglishNLP, detect_language, tokenize, transliterate, remove_stopwords

nlp = HinglishNLP()

# Test 1: Language detection
print('=== Language Detection ===')
tests = [
    'Hello, how are you?',
    'kal mai khaana khane gaya',
    'RM: Namaste, ICICI Bank mein aapka swagat hai.',
    'Customer: My account has been frozen.',
    'aaj mausam bahut acha hai',
]
for t in tests:
    print(f'  {t[:50]:50s} -> {nlp.detect(t)}')

# Test 2: Tokenization
print()
print('=== Tokenization ===')
print(f'  hinglish: {nlp.tokenize("kal mai khaana khane gaya")}')
print(f'  english:  {nlp.tokenize("hello how are you")}')

# Test 3: Sentence splitting
print()
print('=== Sentence Splitting ===')
print(f'  {nlp.tokenize_sentences("Kal mai bazaar gaya. Wahan bahut bheed thi. Phir ghar aa gaya.")}')

# Test 4: Stop words
print()
print('=== Stop Words ===')
tokens = nlp.tokenize('kal mai khaana khane gaya aur bahut maza aaya')
print(f'  before: {tokens}')
print(f'  after:  {nlp.remove_stopwords(tokens)}')

# Test 5: Transliteration
print()
print('=== Transliteration ===')
dev = nlp.transliterate('kal mai khaana khane gaya')
print(f'  {dev}')

# Test 6: Full pipeline
print()
print('=== Pipeline ===')
result = nlp.pipeline('aaj mausam bahut acha hai')
for k, v in result.items():
    print(f'  {k}: {v}')
