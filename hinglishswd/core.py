from hinglishswd.detect import detect_language
from hinglishswd.tokenize import tokenize, tokenize_sentences
from hinglishswd.transliterate import hinglish_to_devanagari
from hinglishswd.translate import hinglish_to_english, translate_pipeline
from hinglishswd.stopwords import remove_stopwords

class HinglishNLP:
    def detect(self, text):
        return detect_language(text)

    def tokenize(self, text, lang=None):
        return tokenize(text, lang)

    def tokenize_sentences(self, text):
        return tokenize_sentences(text)

    def transliterate(self, text):
        return hinglish_to_devanagari(text)

    def translate(self, text):
        return hinglish_to_english(text)

    def translate_pipeline(self, text):
        return translate_pipeline(text)

    def remove_stopwords(self, tokens, lang="hinglish"):
        return remove_stopwords(tokens, lang)

    def pipeline(self, text):
        lang = self.detect(text)
        sentences = self.tokenize_sentences(text)
        tokens = self.tokenize(text, lang)
        cleaned_tokens = self.remove_stopwords(tokens, lang if lang != "english" else "hinglish")
        devanagari = self.transliterate(text) if lang not in ("english", "unknown") else None
        english = self.translate(text) if lang != "english" else text
        return {
            "text": text,
            "language": lang,
            "sentences": sentences,
            "tokens": tokens,
            "tokens_no_stopwords": cleaned_tokens,
            "devanagari": devanagari,
            "english": english,
        }
