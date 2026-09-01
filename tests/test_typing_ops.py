from src.typing_ops import (
    get_first_item, process_mapping, apply_function,
    add_elements, parse_status, filter_sequence,
    format_user_info, calculate_total, identity_generator,
    merge_dictionaries
)

def test_typing_operations():
    # 1. get_first_item
    assert get_first_item([1, 2, 3]) == 1
    assert get_first_item([]) is None
    
    # 2. process_mapping
    assert process_mapping({"a": 1, "b": "text"}) == ["a: 1", "b: text"]
    
    # 3. apply_function
    assert apply_function(lambda x: x * 2, 5) == 10
    
    # 4. add_elements (TypeVar)
    assert add_elements(5, 10) == 15
    assert add_elements("Hello, ", "World!") == "Hello, World!"
    
    # 5. parse_status (Literal)
    assert parse_status("active") == "Status is active"
    
    # 6. filter_sequence (Sequence)
    assert filter_sequence([1, 5, 10, 15], 8) == [10, 15]
    
    # 7. format_user_info (Optional)
    assert format_user_info("Sudenaz") == "User: Sudenaz"
    assert format_user_info("Sudenaz", 21) == "User: Sudenaz, Age: 21"
    
    # 8. calculate_total (list[float])
    assert calculate_total([10.5, 20.0, 4.5]) == 35.0
    
    # 9. identity_generator (TypeVar generic test)
    assert identity_generator(100) == 100
    assert identity_generator("test") == "test"
    
    # 10. merge_dictionaries (TypeVar generic dict test)
    d1 = {"x": 1, "y": 2}
    d2 = {"y": 3, "z": 4}
    assert merge_dictionaries(d1, d2) == {"x": 1, "y": 3, "z": 4}