from collections.abc import Generator


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    if n <= 0:
        return
        
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b