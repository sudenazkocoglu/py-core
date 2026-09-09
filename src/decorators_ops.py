import os
import time
import types
import inspect
import functools
from collections.abc import Callable
from functools import wraps
from pathlib import Path
from typing import Any, TypeVar, cast
from typing_extensions import Self

F = TypeVar("F", bound=Callable[..., Any])

# 1. measure_execution_time
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

# 2. retry_on_exception
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

# 3. memoize
def memoize(func: F) -> F:
    cache: dict[tuple[Any, ...], Any] = {}
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return cast(F, wrapper)

# 4. log_calls
def log_calls(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling '{func.__name__}({signature})'")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned {result!r}")
        return result
    return cast(F, wrapper)

# 5. validate_types
def validate_types(**expected_types: Any) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            for arg_name, arg_value in bound_args.arguments.items():
                if arg_name in expected_types:
                    expected_type = expected_types[arg_name]
                    if not isinstance(arg_value, expected_type):
                        raise TypeError(
                            f"Argument '{arg_name}' must be of type {expected_type.__name__}, got {type(arg_value).__name__}"
                        )
            return func(*args, **kwargs)
        return cast(F, wrapper)
    return decorator

# 6. TimerContext (Context Manager 1)
class TimerContext:
    def __init__(self) -> None:
        self.start_time: float = 0.0
        self.elapsed: float = 0.0

    def __enter__(self) -> Self:
        self.start_time = time.perf_counter()
        return self 

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None:
        self.elapsed = time.perf_counter() - self.start_time

# 7. SuppressException (Context Manager 2)
class SuppressException:
    def __init__(self, *exceptions: type[Exception]) -> None:
        self.exceptions = exceptions

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> bool:
        return exc_type is not None and issubclass(exc_type, self.exceptions)

# 8. ChangeDirectory (Context Manager 3)
class ChangeDirectory:
    def __init__(self, new_path: str | Path) -> None:
        self.new_path = Path(new_path)
        self.original_path: Path = Path()

    def __enter__(self) -> Self:
        self.original_path = Path.cwd()
        os.chdir(self.new_path)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None:
        os.chdir(self.original_path)

# 9. TransactionContext (Context Manager 4)
class TransactionContext:
    def __init__(self) -> None:
        self.state: str = "IDLE"

    def __enter__(self) -> Self:
        self.state = "ACTIVE"
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None:
        if exc_type is not None:
            self.state = "ROLLED_BACK"
        else:
            self.state = "COMMITTED"

# 10. RateLimiterContext (Context Manager 5 - Eksik olan 10. tanım tamamlandı)
class RateLimiterContext:
    def __init__(self, delay: float = 0.05) -> None:
        self.delay = delay

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None:
        time.sleep(self.delay)