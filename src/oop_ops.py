import math
from typing import Any
from dataclasses import dataclass
from abc import ABC, abstractmethod

# 1. Encapsulation (Kapsülleme)
class BankAccount:
    """Banka hesabı simülasyonu. Bakiye gizli (private) tutulur."""
    
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.__balance = initial_balance  # Private değişken

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Yatırılacak miktar pozitif olmalıdır.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Çekilecek miktar pozitif olmalıdır.")
        if amount > self.__balance:
            raise ValueError("Yetersiz bakiye.")
        self.__balance -= amount


# 2. Inheritance & Polymorphism (Kalıtım ve Çok Biçimlilik)
class Shape:
    """Geometrik şekiller için temel sınıf."""
    def area(self) -> float:
        raise NotImplementedError("Alt sınıflar bu metodu ezmelidir (override).")

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


# 3. Dunder/Magic Methods (Sihirli Metotlar)
class Vector:
    """2 Boyutlu bir vektör sınıfı. Operatör aşırı yükleme (overloading) içerir."""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

# 4. Property (Getter/Setter Alternatifi)
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return (self.celsius * 9 / 5) + 32

# 5. Class Methods (Sınıf Metotları / Factory Pattern)
class User:
    def __init__(self, username: str, birth_year: int):
        self.username = username
        self.birth_year = birth_year

    @classmethod
    def from_string(cls, data: str) -> "User":
        # "kullanici-2000" formatındaki stringi parçalayıp nesne üretir
        username, year = data.split("-")
        return cls(username, int(year))

# 6. Data Classes (Veri Sınıfları)
@dataclass
class InventoryItem:
    name: str
    price: float
    quantity: int

    def total_value(self) -> float:
        return self.price * self.quantity

# 7. Gelişmiş Dunder (__repr__) ve Property Setter
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.__salary = salary

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float) -> int | float:
        if value < 0:
            raise ValueError("Maaş negatif olamaz.")
        self.__salary = value

    def __repr__(self) -> str:
        return f"Employee(name='{self.name}', salary={self.__salary})"

# 8. Abstract Base Classes (ABC)
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> str:
        pass

class CarVehicle(Vehicle):
    def start_engine(self) -> str:
        return "Car engine started"

# 9. Static Methods (Statik Metotlar)
class MathUtils:
    @staticmethod
    def is_even(n: int) -> bool:
        return n % 2 == 0

# 10. Custom Iterator (__iter__, __next__)
class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# 11. Composition (Kompozisyon)
class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

class ModernCar:
    def __init__(self, model: str, horsepower: int):
        self.model = model
        self.engine = Engine(horsepower)

# 12. Custom Exception (Özel Hata Sınıfı)
class InvalidAgeError(Exception):
    pass

class Person:
    def __init__(self, age: int):
        if age < 0:
            raise InvalidAgeError("Yaş negatif olamaz.")
        self.age = age

# 13. Slots (__slots__ ile Bellek Optimizasyonu)
class PointedItem:
    __slots__ = ('x', 'y')
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# 14. Property Deleter (@price.deleter)
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.deleter
    def price(self) -> None:
        self._price = 0.0

# 15. Callable Object (__call__ dunder metodu)
class Greeter:
    def __init__(self, greeting: str):
        self.greeting = greeting

    def __call__(self, name: str) -> str:
        return f"{self.greeting}, {name}!"