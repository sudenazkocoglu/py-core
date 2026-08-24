
def reverse_string(text: str) -> str:
    return text[::-1]


def is_palindrome(text: str) -> bool:
    return text == text[::-1]
    