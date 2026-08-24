from src.strings import (
    capitalize_words,
    count_vowels,
    count_words,
    is_anagram,
    is_palindrome,
    reverse_string,
    truncate_string,
)


def test_reverse_string() -> None:
    assert reverse_string("merhaba") == "abahrem"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""


def test_is_palindrome() -> None:
    assert is_palindrome("kayak") is True
    assert is_palindrome("radar") is True
    assert is_palindrome("merhaba") is False
    assert is_palindrome("") is True


def test_count_vowels() -> None:
    assert count_vowels("merhaba") == 3
    assert count_vowels("Python") == 1
    assert count_vowels("AEIOUaeiou") == 10
    assert count_vowels("xyz") == 0


def test_is_anagram() -> None:
    assert is_anagram("listen", "silent") is True
    assert is_anagram("triangle", "integral") is True
    assert is_anagram("hello", "world") is False
    assert is_anagram("a", "ab") is False


def test_count_words() -> None:
    assert count_words("merhaba dünya") == 2
    assert count_words("python programlama dili") == 3
    assert count_words("   ") == 0
    assert count_words("") == 0


def test_capitalize_words() -> None:
    assert capitalize_words("merhaba dünya") == "Merhaba Dünya"
    assert capitalize_words("python programlama dili") == "Python Programlama Dili"
    assert capitalize_words("") == ""

def test_truncate_string() -> None:
    assert truncate_string("Merhaba Dünya", 7) == "Merhaba..."
    assert truncate_string("Python", 10) == "Python"
    assert truncate_string("Test", 4) == "Test"
    