import math
from typing import Any, Iterator
from dataclasses import dataclass
from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        self.owner = owner
        self.__balance = initial_balance

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

class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Vector:
    def __init__(self, x: float, y: float) -> None:
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

class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return (self.celsius * 9 / 5) + 32

class User:
    def __init__(self, username: str, birth_year: int) -> None:
        self.username = username
        self.birth_year = birth_year

    @classmethod
    def from_string(cls, data: str) -> "User":
        username, year = data.split("-")
        return cls(username, int(year))

@dataclass
class InventoryItem:
    name: str
    price: float
    quantity: int

    def total_value(self) -> float:
        return self.price * self.quantity

class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.__salary = salary

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            raise ValueError("Maaş negatif olamaz.")
        self.__salary = value

    def __repr__(self) -> str:
        return f"Employee(name='{self.name}', salary={self.__salary})"

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> str:
        raise NotImplementedError

class CarVehicle(Vehicle):
    def start_engine(self) -> str:
        return "Car engine started"

class MathUtils:
    @staticmethod
    def is_even(n: int) -> bool:
        return n % 2 == 0

class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower

class ModernCar:
    def __init__(self, model: str, horsepower: int) -> None:
        self.model = model
        self.engine = Engine(horsepower)

class InvalidAgeError(Exception):
    pass

class Person:
    def __init__(self, age: int) -> None:
        if age < 0:
            raise InvalidAgeError("Yaş negatif olamaz.")
        self.age = age

class PointedItem:
    __slots__ = ('x', 'y')
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.deleter
    def price(self) -> None:
        self._price = 0.0

class Greeter:
    def __init__(self, greeting: str) -> None:
        self.greeting = greeting

    def __call__(self, name: str) -> str:
        return f"{self.greeting}, {name}!"