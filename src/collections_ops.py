from collections import defaultdict
from typing import Any, TypeVar

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

U = TypeVar('U')

def invert_dict(dictionary: dict[T, U]) -> dict[U, T]:
    return {value: key for key, value in dictionary.items()}

def rotate_list(items: list[T], k: int) -> list[T]:
    if not items:
        return []
    
    k = k % len(items)
    if k == 0:
        return items
        
    return items[-k:] + items[:-k]

def get_list_difference(list1: list[T], list2: list[T]) -> list[T]:
    set2 = set(list2)
    return [item for item in list1 if item not in set2]

def group_dicts_by_key(items: list[dict[str, U]], key: str) -> dict[U, list[dict[str, U]]]:
    grouped: defaultdict[U, list[dict[str, U]]] = defaultdict(list)
    for item in items:
        group_key = item[key]
        grouped[group_key].append(item)
    return dict(grouped)

def deep_merge_dicts(d1: dict[str, Any], d2: dict[str, Any]) -> dict[str, Any]:
    result = d1.copy()
    for key, value in d2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

def sort_dicts_by_key(items: list[dict[str, Any]], key: str, reverse: bool = False) -> list[dict[str, Any]]:
    return sorted(items, key=lambda x: x[key], reverse=reverse)

def get_dict_intersection(d1: dict[str, Any], d2: dict[str, Any]) -> dict[str, Any]:
    return {k: d1[k] for k in d1 if k in d2 and d1[k] == d2[k]}