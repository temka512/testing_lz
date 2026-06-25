import pytest
from testing import function_abf

def test_1():
    result = function_abf(10, 6, 9)
    assert result == 3.5

def test_2():
    assert function_abf(5, 5, 4) == "a не должно быть равно b (деление на ноль)"

def test_3():
    assert function_abf(3, 5, 4) == "a-b должно быть больше 0 (для извлечения корня)"

def test_4():
    assert function_abf(10, 6, -4) == "f должно быть больше 0 (для извлечения корня)"             

def test_5():
    result = function_abf(10, 6, 0)
    assert result == 0.5

def test_6():
    with pytest.raises(TypeError):
        function_abf("10", 6, 9)

def test_7():
    with pytest.raises(TypeError):
        function_abf(10, 6, "9")

def test_8():
    result = function_abf(3.5, 1.25, 0.25)
    assert abs(result - 1.1666666666666667) < 0.000000001

def test_9():
    result = function_abf(1000000000004, 1000000000000, 16)
    assert result == 4.5
