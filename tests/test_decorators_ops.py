import time
from pathlib import Path

import pytest

from src.decorators_ops import (
    ChangeDirectory,
    SuppressException,
    TimerContext,
    log_calls,
    measure_execution_time,
    memoize,
    retry_on_exception,
    validate_types,
)


def test_retry_on_exception() -> None:
    attempts = 0

    @retry_on_exception(exception=ValueError, retries=3, delay=0.01)
    def unstable_task() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("Geçici hata")
        return "başarılı"

    result = unstable_task()
    assert result == "başarılı"
    assert attempts == 3

    # Belirtilen deneme hakkı aşılırsa hata fırlatmalı
    @retry_on_exception(exception=ValueError, retries=2, delay=0.01)
    def always_fails() -> None:
        raise ValueError("Kalıcı hata")

    with pytest.raises(ValueError):
        always_fails()


def test_measure_execution_time(capsys: pytest.CaptureFixture[str]) -> None:
    @measure_execution_time
    def dummy_task(sleep_time: float) -> str:
        time.sleep(sleep_time)
        return "done"

    result = dummy_task(0.05)
    
    # Orijinal fonksiyon değerini doğru döndürmeli
    assert result == "done"
    
    # Konsola süre ile ilgili bir çıktı basmış olmalı
    captured = capsys.readouterr()
    assert "Execution time" in captured.out or "dummy_task" in captured.out

def test_memoize() -> None:
    call_count = 0

    @memoize
    def expensive_computation(x: int) -> int:
        nonlocal call_count
        call_count += 1
        return x * 2

    # İlk çağrılarda hesaplama yapılır
    assert expensive_computation(5) == 10
    assert call_count == 1

    # Aynı argümanla tekrar çağrıldığında cache'ten döner, count artmaz
    assert expensive_computation(5) == 10
    assert call_count == 1

    # Farklı argümanla çağrıldığında yeniden hesaplanır
    assert expensive_computation(10) == 20
    assert call_count == 2

def test_log_calls(capsys: pytest.CaptureFixture[str]) -> None:
    @log_calls
    def multiply(a: int, b: int) -> int:
        return a * b

    result = multiply(4, 5)
    
    # Orijinal sonuç doğru dönmeli
    assert result == 20
    
    # Konsola fonksiyon adı, argümanlar ve sonuç yazdırılmış olmalı
    captured = capsys.readouterr()
    assert "multiply" in captured.out
    assert "4" in captured.out
    assert "5" in captured.out
    assert "20" in captured.out

def test_validate_types() -> None:
    @validate_types(a=int, b=str)
    def repeat_string(a: int, b: str) -> str:
        return b * a

    # Doğru tiplerle çağrıldığında sorunsuz çalışmalı
    assert repeat_string(3, "abc") == "abcabcabc"

    # Yanlış tip gönderildiğinde TypeError fırlatmalı
    with pytest.raises(TypeError):
        repeat_string("3", "abc")  # type: ignore

    with pytest.raises(TypeError):
        repeat_string(3, 123)  # type: ignore

def test_timer_context() -> None:
    with TimerContext() as timer:
        time.sleep(0.05)
    
    # Süre ölçülmüş ve 0'dan büyük olmalı
    assert timer.elapsed >= 0.04

def test_suppress_exception() -> None:
    # Belirtilen hata türü bastırılmalı ve kod blok boyunca akmaya devam etmeli
    with SuppressException(ValueError):
        raise ValueError("Bu hata bastırılacak")
    
    # Başka türde bir hata gelirse bastırılmamalı ve dışarı fırlatılmalı
    with pytest.raises(TypeError), SuppressException(ValueError):
        raise TypeError("Bu hata bastırılmayacak")

def test_change_directory(tmp_path: Path) -> None:
    original_dir = Path.cwd()
    
    # Geçici bir dizine geçiş yapalım
    with ChangeDirectory(tmp_path):
        assert Path.cwd().resolve() == tmp_path.resolve()
    
    # Blok dışına çıkıldığında orijinal dizine geri dönülmeli
    assert Path.cwd().resolve() == original_dir.resolve()