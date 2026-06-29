try:
    from deep_translator import GoogleTranslator
    _HAS_TRANSLATOR = True
except ImportError:
    _HAS_TRANSLATOR = False

from hinglishswd.transliterate import hinglish_to_devanagari

def to_english(text, source="auto"):
    if not _HAS_TRANSLATOR:
        raise ImportError(
            "deep-translator is required for translation. "
            "Install it with: pip install deep-translator"
        )
    text = str(text).strip()
    if not text:
        return text
    translator = GoogleTranslator(source=source, target="en")
    return translator.translate(text)

def hinglish_to_english(text):
    return to_english(text, source="hi")

def translate_pipeline(text):
    lang = None
    from hinglishswd.detect import detect_language
    lang = detect_language(text)
    if lang == "english":
        return {"original": text, "language": "english", "english": text, "devanagari": None}
    dev_text = hinglish_to_devanagari(text) if lang != "hindi" else text
    english = to_english(dev_text, source="hi")
    return {
        "original": text,
        "language": lang,
        "devanagari": dev_text,
        "english": english,
    }
