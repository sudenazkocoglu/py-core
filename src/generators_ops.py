from collections.abc import Callable, Generator, Iterable
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')


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

def filter_generator(iterable: Iterable[T], predicate: Callable[[T], bool]) -> Generator[T, None, None]:
    for item in iterable:
        if predicate(item):
            yield item

def map_generator(iterable: Iterable[T], mapper: Callable[[T], U]) -> Generator[U, None, None]:
    for item in iterable:
        yield mapper(item)

def chain_generators(*iterables: Iterable[T]) -> Generator[T, None, None]:
    for iterable in iterables:
        yield from iterable 