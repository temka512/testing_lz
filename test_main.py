from testing import function_abf

def test_1():
    result = function_abf(10, 6, 9)
    assert result == 3.5

def test_2():
    result = function_abf(5, 5, 4)
    assert function_abf(5, 5, 4) == "a не должно быть равно b (деление на ноль)"

def test_3():
    assert function_abf(3, 5, 4) == "a-b должно быть больше 0 (для извлечения корня)"

def test_4():
    assert function_abf(10, 6, -4) == "f должно быть больше 0 (для извлечения корня)"             

def test_5():
    result = function_abf(10, 6, 0)
    assert result == 0.5
