from collections import deque
from collections.abc import Callable, Generator, Iterable
from itertools import combinations, islice, permutations, product
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

def generate_combinations(iterable: Iterable[T], r: int) -> Generator[tuple[T, ...], None, None]:
    yield from combinations(iterable, r)

def generate_permutations(iterable: Iterable[T], r: int | None = None) -> Generator[tuple[T, ...], None, None]:
    yield from permutations(iterable, r)

def generate_cartesian_product(*iterables: Iterable[T]) -> Generator[tuple[T, ...], None, None]:
    yield from product(*iterables)

def chunk_generator(iterable: Iterable[T], chunk_size: int) -> Generator[tuple[T, ...], None, None]:
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    
    iterator = iter(iterable)
    while True:
        batch = list(islice(iterator, chunk_size))
        if not batch:
            break
        yield tuple(batch)

def moving_average_generator(iterable: Iterable[float], window_size: int) -> Generator[float, None, None]:
    if window_size <= 0:
        raise ValueError("Window size must be greater than zero.")
    
    iterator = iter(iterable)
    window: deque[float] = deque(maxlen=window_size)
    
    # İlk pencereyi doldur
    for _ in range(window_size):
        try:
            window.append(next(iterator))
        except StopIteration:
            return  # Veri pencere boyutundan küçükse hiç değer üretme
            
    # İlk ortalamayı ver
    yield sum(window) / window_size
    
    # Kalan elemanlar için kayarak devam et
    for item in iterator:
        window.append(item)
        yield sum(window) / window_size