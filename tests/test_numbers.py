from src.numbers import factorial, is_prime


def test_is_prime() -> None:
    assert is_prime(2) is True
    assert is_prime(11) is True
    assert is_prime(4) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False

def test_factorial() -> None:
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720