import pytest
from src.typing_ops import (
    get_first_item, process_mapping, apply_function,
    add_elements, parse_status, filter_sequence,
    format_user_info, calculate_total, identity_generator,
    merge_dictionaries
)

@pytest.mark.parametrize("girdi,beklenen", [
    ([1, 2, 3], 1),
    ([], None)
])
def test_get_first_item(girdi, beklenen):
    assert get_first_item(girdi) == beklenen

def test_process_mapping():
    assert process_mapping({"a": 1, "b": "text"}) == ["a: 1", "b: text"]

def test_apply_function():
    assert apply_function(lambda x: x * 2, 5) == 10

@pytest.mark.parametrize("val1,val2,beklenen", [
    (5, 10, 15),
    ("Hello, ", "World!", "Hello, World!")
])
def test_add_elements(val1, val2, beklenen):
    assert add_elements(val1, val2) == beklenen

def test_parse_status():
    assert parse_status("active") == "Status is active"

def test_filter_sequence():
    assert filter_sequence([1, 5, 10, 15], 8) == [10, 15]

def test_format_user_info():
    assert format_user_info("Sudenaz") == "User: Sudenaz"
    assert format_user_info("Sudenaz", 21) == "User: Sudenaz, Age: 21"

def test_calculate_total():
    assert calculate_total([10.5, 20.0, 4.5]) == 35.0

@pytest.mark.parametrize("deger", [100, "test"])
def test_identity_generator(deger):
    assert identity_generator(deger) == deger

def test_merge_dictionaries():
    d1 = {"x": 1, "y": 2}
    d2 = {"y": 3, "z": 4}
    assert merge_dictionaries(d1, d2) == {"x": 1, "y": 3, "z": 4}