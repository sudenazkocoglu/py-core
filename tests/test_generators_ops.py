from src.generators_ops import fibonacci_generator, infinite_counter


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