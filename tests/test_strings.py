from src.strings import reverse_string

def test_reverse_string() -> None:
    assert reverse_string("merhaba") == "abahrem"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
