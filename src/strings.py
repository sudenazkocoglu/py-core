import re
import unicodedata


def reverse_string(text: str) -> str:
    return text[::-1]


def is_palindrome(text: str) -> bool:
    return text == text[::-1]


def count_vowels(text: str) -> int:
    vowels = set("aeiouAEIOUıİöÖüÜ")
    return sum(1 for char in text if char in vowels)


def is_anagram(text1: str, text2: str) -> bool:
    return sorted(text1.lower()) == sorted(text2.lower())


def count_words(text: str) -> int:
    return len(text.split())


def capitalize_words(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split())


def truncate_string(text: str, max_length: int) -> str:
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def slugify(text: str) -> str:
    # Türkçe karakterleri İngilizce karşılıklarına dönüştür
    tr_chars = str.maketrans("çğışüöÇĞİŞÜÖ", "cgisuoCGISUO")
    text = text.translate(tr_chars)
    # Aksanları temizle ve ASCII'ye çevir
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    # Alfanumerik olmayan karakterleri kaldır, boşlukları tire ile değiştir
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text

def longest_word(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

def remove_duplicates(text: str) -> str:
    return "".join(dict.fromkeys(text))
    

