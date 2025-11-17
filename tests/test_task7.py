from src.task7 import set_operations

def test_set_operations():
    ops = set_operations({1, 2, 3}, {3, 4})
    assert ops["union"] == {1, 2, 3, 4}
    assert ops["intersection"] == {3}
    assert ops["difference"] == {1, 2}
    assert ops["symmetric_difference"] == {1, 2, 4}
