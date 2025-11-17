from src.task6 import newton_symbol

def test_newton_symbol():
    assert newton_symbol(5, 2) == 10
    assert newton_symbol(6, 3) == 20
    assert newton_symbol(0, 0) == 1
