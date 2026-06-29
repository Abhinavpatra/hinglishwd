import re

try:
    from indic_transliteration import sanscript
    _HAS_INDIC = True
except ImportError:
    _HAS_INDIC = False

_HINGLISH_TO_ITRANS = [
    (r"sh(?=[^r])", "sh"),
    (r"Sh", "Sh"),
    (r"ch", "ch"),
    (r"Ch", "Ch"),
    (r"kh", "kh"),
    (r"gh", "gh"),
    (r"jh", "jh"),
    (r"th(?![aeiou])", "th"),
    (r"dh", "dh"),
    (r"ph", "ph"),
    (r"bh", "bh"),
    (r"ng", "ng"),
    (r"ny", "ny"),
    (r"n(?=[gk])", "N"),
    (r"T", "T"),
    (r"D", "D"),
    (r"N", "N"),
    (r"oo", "U"),
    (r"ee", "I"),
    (r"aa", "A"),
    (r"ii", "I"),
    (r"uu", "U"),
    (r"ai", "ai"),
    (r"au", "au"),
    (r"ri", "Ri"),
    (r"rr", "RRi"),
    (r"lr", "Li"),
]

def _hinglish_to_itrans(text):
    text = text.lower()
    for pattern, replacement in _HINGLISH_TO_ITRANS:
        text = re.sub(pattern, replacement, text)
    return text

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
        itrans_text = _hinglish_to_itrans(text)
        return sanscript.transliterate(itrans_text, _from=sanscript.ITRANS, _to=sanscript.DEVANAGARI)
    elif to_script == "itrans":
        return sanscript.transliterate(text, _from=sanscript.DEVANAGARI, _to=sanscript.ITRANS)
    else:
        raise ValueError(f"Unknown script: {to_script}. Use 'devanagari' or 'itrans'.")

def hinglish_to_devanagari(text):
    return transliterate(text, "devanagari")
