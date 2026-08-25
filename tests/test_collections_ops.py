from src.collections_ops import flatten_list, get_frequencies


def test_flatten_list() -> None:
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([["a", "b"], ["c"]]) == ["a", "b", "c"]
    assert flatten_list([[], [1, 2]]) == [1, 2]
    assert flatten_list([]) == []

def test_get_frequencies() -> None:
    assert get_frequencies(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}
    assert get_frequencies([1, 1, 1, 1]) == {1: 4}
    assert get_frequencies([]) == {}