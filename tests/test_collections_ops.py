from src.collections_ops import flatten_list


def test_flatten_list() -> None:
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([["a", "b"], ["c"]]) == ["a", "b", "c"]
    assert flatten_list([[], [1, 2]]) == [1, 2]
    assert flatten_list([]) == []