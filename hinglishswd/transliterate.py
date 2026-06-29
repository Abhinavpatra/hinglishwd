try:
    from indic_transliteration import sanscript
    _HAS_INDIC = True
except ImportError:
    _HAS_INDIC = False

def transliterate(text, to_script="devanagari"):
    if not _HAS_INDIC:
        raise ImportError(
            "indic-transliteration is required for transliteration. "
            "Install it with: pip install indic-transliteration"
        )
    text = str(text).strip()
    if not text:
        return text
    if to_script == "devanagari":
        return sanscript.transliterate(text, _from=sanscript.ITRANS, _to=sanscript.DEVANAGARI)
    elif to_script == "itrans":
        return sanscript.transliterate(text, _from=sanscript.DEVANAGARI, _to=sanscript.ITRANS)
    else:
        raise ValueError(f"Unknown script: {to_script}. Use 'devanagari' or 'itrans'.")

def hinglish_to_devanagari(text):
    return transliterate(text, "devanagari")
