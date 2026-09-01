import asyncio
from typing import List, AsyncIterator, Any, Callable, TypeVar

T = TypeVar('T')

async def fetch_data_mock(delay: float, value: str) -> str:
    """Belirtilen süre kadar bekleyip değer döndürür."""
    await asyncio.sleep(delay)
    return value

async def fetch_multiple(tasks_data: List[tuple[float, str]]) -> List[str]:
    """Birden fazla async görevi aynı anda çalıştırır (gather)."""
    tasks = [fetch_data_mock(delay, val) for delay, val in tasks_data]
    return await asyncio.gather(*tasks)

async def fetch_with_timeout(delay: float, timeout: float) -> str:
    """Zaman aşımı (timeout) yönetimi ile veri çeker."""
    try:
        return await asyncio.wait_for(fetch_data_mock(delay, "Success"), timeout=timeout)
    except asyncio.TimeoutError:
        return "Timeout"

async def process_queue(items: List[int]) -> List[int]:
    """Async Queue kullanarak elemanları işler."""
    queue: asyncio.Queue[int] = asyncio.Queue()
    for item in items:
        await queue.put(item)
    
    results: List[int] = []
    while not queue.empty():
        val = await queue.get()
        results.append(val * 2)
        queue.task_done()
    return results

async def rate_limited_fetch(ids: List[int], limit: int) -> List[int]:
    """Semaphore ile eşzamanlılık (rate limit) uygular."""
    semaphore = asyncio.Semaphore(limit)
    async def worker(i: int) -> int:
        async with semaphore:
            await asyncio.sleep(0.01)
            return i * 10
    return await asyncio.gather(*(worker(i) for i in ids))

async def safe_async_call(should_fail: bool) -> str:
    """Hata yönetimi içeren async fonksiyon."""
    if should_fail:
        raise ValueError("Async error")
    await asyncio.sleep(0.01)
    return "OK"

async def async_number_generator(n: int) -> AsyncIterator[int]:
    """Async generator ile sayı üretir."""
    for i in range(n):
        await asyncio.sleep(0.01)
        yield i

class AsyncTimer:
    """Async Context Manager örneği."""
    async def __aenter__(self) -> "AsyncTimer":
        return self
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        pass

async def chain_async_operations(val: int) -> int:
    """Zincirleme async işlemleri çalıştırır."""
    await asyncio.sleep(0.01)
    res1 = val + 5
    await asyncio.sleep(0.01)
    return res1 * 2

async def retry_async_operation(func: Callable[..., Any], retries: int = 3) -> Any:
    """Başarısız olan async işlemi tekrar deneme mekanizması (Retry)."""
    for attempt in range(retries):
        try:
            return await func()
        except Exception:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(0.01)