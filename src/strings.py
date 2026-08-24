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
    

