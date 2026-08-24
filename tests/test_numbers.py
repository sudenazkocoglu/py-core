from src.numbers import is_prime


def test_is_prime() -> None:
    assert is_prime(2) is True
    assert is_prime(11) is True
    assert is_prime(4) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False