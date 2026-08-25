
import pytest

from src.generators_ops import (
    fibonacci_generator,
    filter_generator,
    infinite_counter,
    map_generator,
)

# ... (önceki testler) ...

def test_filter_generator() -> None:
    numbers = [1, 2, 3, 4, 5, 6]
    # Sadece çift sayıları filtreleyen jeneratör
    gen = filter_generator(numbers, lambda x: x % 2 == 0)
    
    assert next(gen) == 2
    assert next(gen) == 4
    assert next(gen) == 6
    
    # Jeneratördeki elemanlar bittiğinde StopIteration hatası fırlatmalı
    with pytest.raises(StopIteration):
        next(gen)
        
    # Boş liste testi (listeye çevirerek hızlıca test edebiliriz)
    empty_gen = filter_generator([], lambda x: x > 0)
    assert list(empty_gen) == []


def test_fibonacci_generator() -> None:
    # İlk 5 Fibonacci sayısını üretip listeye çevirerek kontrol ediyoruz
    assert list(fibonacci_generator(5)) == [0, 1, 1, 2, 3]
    
    # İlk 1 Fibonacci sayısı
    assert list(fibonacci_generator(1)) == [0]
    
    # 0 veya negatif değerler için hiçbir şey üretmemeli
    assert list(fibonacci_generator(0)) == []
    assert list(fibonacci_generator(-3)) == []

def test_infinite_counter() -> None:
    counter = infinite_counter(10, 2)
    assert next(counter) == 10
    assert next(counter) == 12
    assert next(counter) == 14
    
    # Negatif adımla geriye sayım testi
    countdown = infinite_counter(5, -1)
    assert next(countdown) == 5
    assert next(countdown) == 4
    assert next(countdown) == 3

def test_filter_generator() -> None:
    numbers = [1, 2, 3, 4, 5, 6]
    # Sadece çift sayıları filtreleyen jeneratör
    gen = filter_generator(numbers, lambda x: x % 2 == 0)
    
    assert next(gen) == 2
    assert next(gen) == 4
    assert next(gen) == 6
    
    # Jeneratördeki elemanlar bittiğinde StopIteration hatası fırlatmalı
    with pytest.raises(StopIteration):
        next(gen)
        
    # Boş liste testi (listeye çevirerek hızlıca test edebiliriz)
    empty_gen = filter_generator([], lambda x: x > 0)
    assert list(empty_gen) == []

def test_map_generator() -> None:
    numbers = [1, 2, 3, 4]
    # Her sayının karesini alan jeneratör
    gen = map_generator(numbers, lambda x: x ** 2)
    
    assert next(gen) == 1
    assert next(gen) == 4
    assert next(gen) == 9
    assert next(gen) == 16
    
    # Elemanlar bittiğinde StopIteration fırlatmalı
    with pytest.raises(StopIteration):
        next(gen)
        
    # Metin dönüştürme testi (farklı veri tipleriyle çalıştığını doğrulama)
    words = ["hello", "world"]
    upper_gen = map_generator(words, lambda s: s.upper())
    assert list(upper_gen) == ["HELLO", "WORLD"]