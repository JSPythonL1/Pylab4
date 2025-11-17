from src.task3 import filter_above_four

def test_filter_above_four():
    assert filter_above_four([1, 2, 3, 5, 8, 3, 0, 7]) == [5, 8, 7]
