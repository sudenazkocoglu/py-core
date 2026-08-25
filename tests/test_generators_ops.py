
from collections.abc import Generator

import pytest

from src.generators_ops import (
    chain_generators,
    fibonacci_generator,
    filter_generator,
    generate_cartesian_product,
    generate_combinations,
    generate_permutations,
    infinite_counter,
    map_generator,
)


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
    empty_gen: Generator[int, None, None] = filter_generator([], lambda x: x > 0)
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

def test_chain_generators() -> None:
    list1 = [1, 2]
    # Basit bir jeneratör (tuple comprehension)
    gen2 = (x for x in [3, 4]) 
    list3 = [5]
    
    chained = chain_generators(list1, gen2, list3)
    
    assert next(chained) == 1
    assert next(chained) == 2
    assert next(chained) == 3
    assert next(chained) == 4
    assert next(chained) == 5
    
    # Elemanlar bittiğinde StopIteration fırlatmalı
    import pytest
    with pytest.raises(StopIteration):
        next(chained)
        
    # Boş yapılarla test
    assert list(chain_generators([], [], [99])) == [99]
    assert list(chain_generators()) == []

def test_generate_combinations() -> None:
    items = ["A", "B", "C"]
    # 2'li kombinasyonları üreten jeneratör
    gen = generate_combinations(items, 2)
    
    assert next(gen) == ("A", "B")
    assert next(gen) == ("A", "C")
    assert next(gen) == ("B", "C")
    
    # Elemanlar bittiğinde StopIteration fırlatmalı
    import pytest
    with pytest.raises(StopIteration):
        next(gen)
        
    # Boş liste veya tek elemanlı liste testleri
    assert list(generate_combinations([], 2)) == []
    assert list(generate_combinations(["A"], 2)) == []

def test_generate_permutations() -> None:
    items = ["A", "B"]
    # 2'li permütasyonları üreten jeneratör
    gen = generate_permutations(items, 2)
    
    assert next(gen) == ("A", "B")
    assert next(gen) == ("B", "A")
    
    # Elemanlar bittiğinde StopIteration fırlatmalı
    with pytest.raises(StopIteration):
        next(gen)
        
    # Boş liste veya geçersiz uzunluk testleri
    assert list(generate_permutations([], 2)) == []

def test_generate_cartesian_product() -> None:
    pool1 = [1, 2]
    pool2 = ["a", "b"]
    
    # Cartesian çarpım üreten jeneratör
    gen = generate_cartesian_product(pool1, pool2)
    
    assert next(gen) == (1, "a")
    assert next(gen) == (1, "b")
    assert next(gen) == (2, "a")
    assert next(gen) == (2, "b")
    
    # Elemanlar bittiğinde StopIteration fırlatmalı
    with pytest.raises(StopIteration):
        next(gen)
        
    # Tek havuz veya boş havuz testleri
    assert list(generate_cartesian_product([1, 2])) == [(1,), (2,)]
    assert list(generate_cartesian_product([], [1, 2])) == []