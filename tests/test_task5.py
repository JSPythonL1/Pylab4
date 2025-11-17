from src.task5 import decorated_add

def test_decorated_add(capsys):
    result = decorated_add(2, 3)
    captured = capsys.readouterr()
    assert "decorated_add" in captured.out
    assert "(2, 3)" in captured.out
    assert result == 5
