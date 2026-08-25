import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])

def measure_execution_time(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' execution time: {elapsed_time:.6f} seconds")
        return result
    return cast(F, wrapper)

def retry_on_exception(exception: type[Exception] = Exception, retries: int = 3, delay: float = 0.1) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(delay)
                    continue
            if last_exception:
                raise last_exception
            raise RuntimeError("Maximum retries reached without success.")
        return cast(F, wrapper)
    return decorator

def memoize(func: F) -> F:
    cache: dict[tuple[Any, ...], Any] = {}
    
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Argümanları anahtar (key) olarak kullanmak için tuple yapısına dönüştürelim
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
        
    return cast(F, wrapper)