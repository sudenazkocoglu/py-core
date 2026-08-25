from src.collections_ops import (
    chunk_list,
    find_common_elements,
    flatten_list,
    get_frequencies,
    invert_dict,
    merge_dicts,
)


def test_flatten_list() -> None:
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([["a", "b"], ["c"]]) == ["a", "b", "c"]
    assert flatten_list([[], [1, 2]]) == [1, 2]
    assert flatten_list([]) == []

def test_get_frequencies() -> None:
    assert get_frequencies(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}
    assert get_frequencies([1, 1, 1, 1]) == {1: 4}
    assert get_frequencies([]) == {}

def test_chunk_list() -> None:
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list(["a", "b", "c"], 1) == [["a"], ["b"], ["c"]]
    assert chunk_list([], 3) == []
    assert chunk_list([1, 2], 5) == [[1, 2]]

def test_merge_dicts() -> None:
    assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 5, "c": 4}
    assert merge_dicts({}, {"x": 10}) == {"x": 10}
    assert merge_dicts({"y": 5}, {}) == {"y": 5}
    assert merge_dicts({}, {}) == {}

def test_find_common_elements() -> None:
    assert sorted(find_common_elements([1, 2, 3], [2, 3, 4])) == [2, 3]
    assert sorted(find_common_elements([1, 1, 2, 2], [1, 2, 3])) == [1, 2]
    assert find_common_elements(["a", "b"], ["c", "d"]) == []
    assert find_common_elements([], [1, 2]) == []

def test_invert_dict() -> None:
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_dict({"x": "y"}) == {"y": "x"}
    assert invert_dict({}) == {}