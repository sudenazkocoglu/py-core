def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Faktöriyel negatif sayılar için tanımlı değildir.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci negatif sayılar için tanımlı değildir.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b) 

def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))

def reverse_number(n: int) -> int:
    if n == 0:
        return 0
    sign = -1 if n < 0 else 1
    reversed_str = str(abs(n))[::-1]
    return sign * int(reversed_str)

def prime_factors(n: int) -> list[int]:
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return n == total