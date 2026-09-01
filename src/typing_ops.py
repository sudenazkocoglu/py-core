from typing import List, Dict, Union, Optional, Callable, Any, TypeVar, Literal, Sequence

T = TypeVar('T', int, float, str)

def get_first_item(items: List[Any]) -> Optional[Any]:
    return items[0] if items else None

def process_mapping(data: Dict[str, Union[int, str]]) -> List[str]:
    return [f"{k}: {v}" for k, v in data.items()]

def apply_function(func: Callable[[int], int], value: int) -> int:
    return func(value)

def add_elements(a: T, b: T) -> T:
    return a + b

def parse_status(status: Literal["active", "inactive", "pending"]) -> str:
    return f"Status is {status}"

def filter_sequence(seq: Sequence[int], threshold: int) -> List[int]:
    return [x for x in seq if x > threshold]

def format_user_info(name: str, age: Optional[int] = None) -> str:
    if age is None:
        return f"User: {name}"
    return f"User: {name}, Age: {age}"

def calculate_total(prices: list[float]) -> float:
    return sum(prices)

def identity_generator(val: T) -> T:
    return val

def merge_dictionaries(d1: Dict[str, T], d2: Dict[str, T]) -> Dict[str, T]:
    """İki sözlüğü birleştirir (TypeVar generic kullanımı)."""
    return {**d1, **d2}