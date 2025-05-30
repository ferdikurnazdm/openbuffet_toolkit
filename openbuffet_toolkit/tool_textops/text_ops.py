import re
import unicodedata

class TextOps:
    """
    Provides static methods for common text cleaning and normalization operations.
    Suitable for NLP and text preprocessing tasks.
    """

    @staticmethod
    def transliterate_turkish(text: str) -> str:
        """
        Converts Turkish-specific characters to their ASCII equivalents.
        """
        translation_table = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
        return text.translate(translation_table)

    @staticmethod
    def normalize_unicode(text: str) -> str:
        """
        Normalizes Unicode characters to their canonical form.
        """
        return unicodedata.normalize('NFKC', text)

    @staticmethod
    def remove_punctuation(text: str) -> str:
        """
        Removes all punctuation characters from the text.
        """
        return re.sub(r"[^\w\s]", "", text)

    @staticmethod
    def simplify_spaces(text: str) -> str:
        """
        Replaces multiple spaces, newlines, and tabs with a single space.
        """
        return re.sub(r"\s+", " ", text)

    @staticmethod
    def clean(
        text: str,
        use_transliterate: bool = True,
        use_unicode: bool = True,
        use_punctuation: bool = True,
        use_spaces: bool = True,
        strip_result: bool = True
    ) -> str:
        """
        Applies a customizable set of text preprocessing steps.

        Args:
            text (str): The input text to clean.
            use_transliterate (bool): Whether to convert Turkish chars to ASCII.
            use_unicode (bool): Whether to normalize Unicode.
            use_punctuation (bool): Whether to remove punctuation.
            use_spaces (bool): Whether to normalize whitespace.
            strip_result (bool): Whether to strip leading/trailing spaces.

        Returns:
            str: Cleaned text based on enabled steps.
        """
        if use_transliterate:
            text = TextOps.transliterate_turkish(text)
        if use_unicode:
            text = TextOps.normalize_unicode(text)
        if use_punctuation:
            text = TextOps.remove_punctuation(text)
        if use_spaces:
            text = TextOps.simplify_spaces(text)
        if strip_result:
            text = text.strip()
        return text
