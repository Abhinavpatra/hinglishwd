# hinglishswd

A Python library for Hinglish (Hindi+English code-mixed) NLP.

## Features

- **Language detection** — English / Hindi (Devanagari) / Hinglish (Latin-script Hindi)
- **Tokenization** — Punctuation-aware splitting for Hinglish, spaCy-based for Devanagari Hindi
- **Transliteration** — Hinglish → Hindi Devanagari (via `indic-transliteration`)
- **Translation** — Hinglish/Hindi → English (via `deep-translator` Google Translate)
- **Stop word removal** — Built-in Hindi + Hinglish stop word lists
- **Pipeline API** — Single-call for full processing

## Installation

```bash
pip install hinglishswd
```

## Quick Start

```python
from hinglishswd import HinglishNLP

nlp = HinglishNLP()

# Language detection
nlp.detect("kal mai khaana khane gaya")    # "hinglish"
nlp.detect("Hello, how are you?")           # "english"
nlp.detect("आज मौसम बहुत अच्छा है")         # "hindi"

# Tokenization
nlp.tokenize("kal mai khaana khane gaya")   # ['kal', 'mai', 'khaana', 'khane', 'gaya']

# Transliteration (Hinglish -> Devanagari)
nlp.transliterate("kal mai khaana khane gaya")  # कल मै खान खने गय

# Translation (Hinglish -> English)
nlp.translate("kal mai khaana khane gaya")  # "I went to eat yesterday"

# Full pipeline
result = nlp.pipeline("aaj mausam bahut acha hai")
# {
#   "text": "aaj mausam bahut acha hai",
#   "language": "hinglish",
#   "tokens": ["aaj", "mausam", "bahut", "acha", "hai"],
#   "tokens_no_stopwords": ["aaj", "mausam", "acha"],
#   "devanagari": "आज मौसम बहुत अच्छा है",
#   "english": "the weather is very good today"
# }
```

## Module-level API

```python
from hinglishswd import (
    detect_language,
    tokenize, tokenize_sentences,
    transliterate, hinglish_to_devanagari,
    to_english, hinglish_to_english, translate_pipeline,
    remove_stopwords,
)

lang = detect_language("Aap kahan ho?")
tokens = tokenize("Mujhe paani chahiye")
dev = hinglish_to_devanagari("mera naam rahul hai")
en = hinglish_to_english("aaj kya kar rahe ho?")
```

## Package Structure

```
hinglishswd/
├── __init__.py
├── core.py              # HinglishNLP class (main API)
├── detect.py            # Language detection
├── tokenize.py          # Tokenization
├── transliterate.py     # Script conversion (Indic-transliteration)
├── translate.py         # Translation (deep-translator)
└── stopwords.py         # Hindi + Hinglish stop words
```

## Dependencies

- `indic-transliteration` — Hinglish ↔ Devanagari transliteration
- `deep-translator` — Google Translate-based translation (optional, for `.translate()`)

## License

MIT
