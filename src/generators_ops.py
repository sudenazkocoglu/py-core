from collections.abc import Generator


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    if n <= 0:
        return
        
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def infinite_counter(start: int, step: int = 1) -> Generator[int, None, None]:
    current = start
    while True:
        yield current
        current += step