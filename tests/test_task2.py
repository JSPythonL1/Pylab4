from src.task2 import squares_to_x

def test_squares_to_x():
    assert squares_to_x(1) == [1]
    assert squares_to_x(3) == [1, 4, 9]
