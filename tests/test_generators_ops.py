from src.generators_ops import fibonacci_generator


def test_fibonacci_generator() -> None:
    # İlk 5 Fibonacci sayısını üretip listeye çevirerek kontrol ediyoruz
    assert list(fibonacci_generator(5)) == [0, 1, 1, 2, 3]
    
    # İlk 1 Fibonacci sayısı
    assert list(fibonacci_generator(1)) == [0]
    
    # 0 veya negatif değerler için hiçbir şey üretmemeli
    assert list(fibonacci_generator(0)) == []
    assert list(fibonacci_generator(-3)) == []