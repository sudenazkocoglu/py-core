from src.strings import count_vowels, is_palindrome, reverse_string


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
    