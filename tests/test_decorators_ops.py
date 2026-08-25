import time

import pytest

from src.decorators_ops import measure_execution_time


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