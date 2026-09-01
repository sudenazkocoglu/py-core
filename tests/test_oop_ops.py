import pytest
from src.oop_ops import (
    BankAccount, Shape, Circle, Rectangle, Vector, Temperature,
    User, InventoryItem, Employee, CarVehicle, MathUtils,
    Countdown, ModernCar, Person, InvalidAgeError, PointedItem, Product, Greeter
)

def test_bank_account_encapsulation():
    account = BankAccount("Sudenaz", 100.0)
    assert account.get_balance() == 100.0
    
    account.deposit(50.0)
    assert account.get_balance() == 150.0
    
    account.withdraw(70.0)
    assert account.get_balance() == 80.0
    
    # Hata durumları
    with pytest.raises(ValueError):
        account.withdraw(500.0)
    
    with pytest.raises(ValueError):
        account.deposit(-20.0)

def test_shape_inheritance():
    circle = Circle(radius=5.0)
    assert round(circle.area(), 2) == 78.54
    
    rectangle = Rectangle(width=4.0, height=6.0)
    assert rectangle.area() == 24.0
    
    # Temel sınıfın doğrudan kullanımı hata fırlatmalı
    base_shape = Shape()
    with pytest.raises(NotImplementedError):
        base_shape.area()

def test_vector_magic_methods():
    v1 = Vector(2, 3)
    v2 = Vector(4, -1)
    
    # Toplama (__add__)
    v3 = v1 + v2
    assert v3.x == 6 and v3.y == 2
    
    # Eşitlik (__eq__)
    assert v1 == Vector(2, 3)
    assert v1 != v2
    
    # String temsili (__str__)
    assert str(v1) == "Vector(2, 3)"

def test_temperature_property():
    temp = Temperature(celsius=0)
    assert temp.fahrenheit == 32.0
    
    # Celsius değiştiğinde fahrenheit property'si otomatik olarak güncel değeri hesaplamalı
    temp.celsius = 100
    assert temp.fahrenheit == 212.0

def test_user_classmethod():
    user = User.from_string("testuser-2000")
    assert user.username == "testuser"
    assert user.birth_year == 2000

def test_inventory_dataclass():
    item1 = InventoryItem(name="Laptop", price=1500.0, quantity=5)
    item2 = InventoryItem(name="Laptop", price=1500.0, quantity=5)
    
    # Dataclass otomatik olarak __eq__ sağlar, manuel yazmaya gerek kalmaz
    assert item1 == item2
    assert item1.total_value() == 7500.0

def test_employee_advanced_oop():
    emp = Employee("Sudenaz", 50000.0)
    assert emp.salary == 50000.0
    
    # Property setter testi
    emp.salary = 60000.0
    assert emp.salary == 60000.0
    
    # Hatalı atama kontrolü
    import pytest
    with pytest.raises(ValueError):
        emp.salary = -1000.0
        
    # __repr__ testi
    assert repr(emp) == "Employee(name='Sudenaz', salary=60000.0)" 

def test_abstract_class():
    car = CarVehicle()
    assert car.start_engine() == "Car engine started"

def test_static_method():
    assert MathUtils.is_even(4) is True
    assert MathUtils.is_even(5) is False

def test_custom_iterator():
    counter = Countdown(3)
    values = list(counter)
    assert values == [3, 2, 1]

def test_composition():
    my_car = ModernCar("Sedan", 150)
    assert my_car.model == "Sedan"
    assert my_car.engine.horsepower == 150

def test_custom_exception():
    with pytest.raises(InvalidAgeError):
        Person(-5)
    p = Person(25)
    assert p.age == 25

def test_slots_usage():
    pt = PointedItem(1.5, 2.5)
    assert pt.x == 1.5 and pt.y == 2.5

def test_property_deleter():
    prod = Product("Laptop", 1500.0)
    assert prod.price == 1500.0
    del prod.price
    assert prod.price == 0.0

def test_callable_object():
    say_hello = Greeter("Merhaba")
    assert say_hello("Sudenaz") == "Merhaba, Sudenaz!"