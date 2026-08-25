from typing import TypeVar

T = TypeVar('T')

def flatten_list(nested_list: list[list[T]]) -> list[T]:
    return [item for sublist in nested_list for item in sublist]

from typing import TypeVar

T = TypeVar('T')

def flatten_list(nested_list: list[list[T]]) -> list[T]:
    return [item for sublist in nested_list for item in sublist]

def get_frequencies(items: list[T]) -> dict[T, int]:
    freq: dict[T, int] = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq