from app import suma

def test_suma():
    assert suma(2, 3) == 5

def test_suma_negativos():
    assert suma(-1, 1) == 0
