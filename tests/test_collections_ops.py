from src.collections_ops import (
    chunk_list,
    deep_merge_dicts,
    find_common_elements,
    flatten_list,
    get_frequencies,
    get_list_difference,
    group_dicts_by_key,
    invert_dict,
    merge_dicts,
    rotate_list,
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

def test_rotate_list() -> None:
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_list(["a", "b", "c"], 1) == ["c", "a", "b"]
    assert rotate_list([1, 2], 5) == [2, 1]  # 5 adım kaydırmak aslında 1 adım kaydırmaktır (5 % 2 = 1)
    assert rotate_list([], 3) == []
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]

def test_get_list_difference() -> None:
    assert get_list_difference([1, 2, 3, 4], [3, 4, 5]) == [1, 2]
    assert get_list_difference(["a", "b"], ["c", "d"]) == ["a", "b"]
    assert get_list_difference([1, 2], [1, 2]) == []
    assert get_list_difference([], [1, 2]) == []

def test_group_dicts_by_key() -> None:
    data = [
        {"cat": "A", "val": 1},
        {"cat": "B", "val": 2},
        {"cat": "A", "val": 3}
    ]
    grouped = group_dicts_by_key(data, "cat")
    assert grouped == {
        "A": [{"cat": "A", "val": 1}, {"cat": "A", "val": 3}],
        "B": [{"cat": "B", "val": 2}]
    }
    assert group_dicts_by_key([], "cat") == {}

def test_deep_merge_dicts() -> None:
    d1 = {"a": {"x": 1}, "b": 2}
    d2 = {"a": {"y": 2}, "c": 3}
    expected = {"a": {"x": 1, "y": 2}, "b": 2, "c": 3}
    assert deep_merge_dicts(d1, d2) == expected
    assert deep_merge_dicts({}, {"x": 1}) == {"x": 1}