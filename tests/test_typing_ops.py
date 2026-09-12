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

@pytest.mark.parametrize("mapping,beklenen", [
    ({"a": 1, "b": "text"}, ["a: 1", "b: text"]),
    ({}, [])
])
def test_process_mapping(mapping, beklenen):
    assert process_mapping(mapping) == beklenen

def test_apply_function():
    assert apply_function(lambda x: x * 2, 5) == 10

@pytest.mark.parametrize("val1,val2,beklenen", [
    (5, 10, 15),
    ("Hello, ", "World!", "Hello, World!")
])
def test_add_elements(val1, val2, beklenen):
    assert add_elements(val1, val2) == beklenen

@pytest.mark.parametrize("status,beklenen", [
    ("active", "Status is active"),
    ("inactive", "Status is inactive")
])
def test_parse_status(status, beklenen):
    assert parse_status(status) == beklenen

@pytest.mark.parametrize("seq,threshold,beklenen", [
    ([1, 5, 10, 15], 8, [10, 15]),
    ([1, 2, 3], 5, [])
])
def test_filter_sequence(seq, threshold, beklenen):
    assert filter_sequence(seq, threshold) == beklenen

@pytest.mark.parametrize("args,beklenen", [
    (("Sudenaz",), "User: Sudenaz"),
    (("Sudenaz", 21), "User: Sudenaz, Age: 21")
])
def test_format_user_info(args, beklenen):
    assert format_user_info(*args) == beklenen

@pytest.mark.parametrize("prices,beklenen", [
    ([10.5, 20.0, 4.5], 35.0),
    ([], 0.0)
])
def test_calculate_total(prices, beklenen):
    assert calculate_total(prices) == beklenen

@pytest.mark.parametrize("deger", [100, "test"])
def test_identity_generator(deger):
    assert identity_generator(deger) == deger

def test_merge_dictionaries():
    d1 = {"x": 1, "y": 2}
    d2 = {"y": 3, "z": 4}
    assert merge_dictionaries(d1, d2) == {"x": 1, "y": 3, "z": 4}
