from src.numbers import (
    factorial,
    fibonacci,
    gcd,
    is_prime,
    lcm,
    reverse_number,
    sum_of_digits,
)


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

def test_fibonacci() -> None:
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

def test_gcd() -> None:
    assert gcd(12, 15) == 3
    assert gcd(24, 36) == 12
    assert gcd(7, 5) == 1
    assert gcd(0, 5) == 5

def test_lcm() -> None:
    assert lcm(4, 6) == 12
    assert lcm(3, 5) == 15
    assert lcm(12, 15) == 60

def test_sum_of_digits() -> None:
    assert sum_of_digits(123) == 6
    assert sum_of_digits(456) == 15
    assert sum_of_digits(0) == 0
    assert sum_of_digits(-123) == 6

def test_reverse_number() -> None:
    assert reverse_number(123) == 321
    assert reverse_number(-456) == -654
    assert reverse_number(120) == 21
    assert reverse_number(0) == 0