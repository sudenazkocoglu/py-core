import asyncio
import pytest
from src.asyncio_ops import (
    fetch_data_mock, fetch_multiple, fetch_with_timeout,
    process_queue, rate_limited_fetch, safe_async_call,
    async_number_generator, AsyncTimer, chain_async_operations,
    retry_async_operation
)

def test_async_operations():
    # 1. fetch_data_mock
    assert asyncio.run(fetch_data_mock(0.01, "hello")) == "hello"

    # 2. fetch_multiple
    results = asyncio.run(fetch_multiple([(0.01, "a"), (0.01, "b")]))
    assert results == ["a", "b"]

    # 3. fetch_with_timeout
    assert asyncio.run(fetch_with_timeout(0.01, 0.1)) == "Success"
    assert asyncio.run(fetch_with_timeout(0.1, 0.01)) == "Timeout"

    # 4. process_queue
    assert asyncio.run(process_queue([1, 2, 3])) == [2, 4, 6]

    # 5. rate_limited_fetch
    assert asyncio.run(rate_limited_fetch([1, 2, 3], 2)) == [10, 20, 30]

    # 6. safe_async_call
    assert asyncio.run(safe_async_call(False)) == "OK"
    with pytest.raises(ValueError):
        asyncio.run(safe_async_call(True))

    # 7. async_number_generator
    async def collect_gen():
        return [num async for num in async_number_generator(3)]
    assert asyncio.run(collect_gen()) == [0, 1, 2]

    # 8. AsyncTimer context manager
    async def test_timer():
        async with AsyncTimer():
            return True
    assert asyncio.run(test_timer()) is True

    # 9. chain_async_operations
    assert asyncio.run(chain_async_operations(10)) == 30  # (10 + 5) * 2

    # 10. retry_async_operation
    attempt_count = 0
    async def unstable_func():
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < 2:
            raise ConnectionError("Fail")
        return "Success"

    assert asyncio.run(retry_async_operation(unstable_func, retries=3)) == "Success"