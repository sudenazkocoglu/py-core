from src.decorators_ops import measure_execution_time, retry_on_exception


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