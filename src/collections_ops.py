from typing import TypeVar

T = TypeVar('T')

def flatten_list(nested_list: list[list[T]]) -> list[T]:
    return [item for sublist in nested_list for item in sublist]

def get_frequencies(items: list[T]) -> dict[T, int]:
    freq: dict[T, int] = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

def chunk_list(items: list[T], size: int) -> list[list[T]]:
    return [items[i:i + size] for i in range(0, len(items), size)]

def merge_dicts(dict1: dict[T, int], dict2: dict[T, int]) -> dict[T, int]:
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

def find_common_elements(list1: list[T], list2: list[T]) -> list[T]:
    return list(set(list1).intersection(set(list2)))