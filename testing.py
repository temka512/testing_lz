def function_abf(a, b, f):
    if a == b:
        return "a не должно быть равно b (деление на ноль)"                 
    if a - b < 0:
        return "a-b должно быть больше 0 (для извлечения корня)"
    if f < 0:
        return "f должно быть больше 0 (для извлечения корня)"              
    return ((a-b)**0.5/(a-b))+f**0.5

#тест 1
print("Тест 1: a=5, b=1, f=9")
result = function_abf(5, 1, 9)
expected = ((5-1)**0.5/(5-1)) + 9**0.5
print(f"Результат: {result}")
print(f"Ожидалось: {expected}")
print(f"Тест пройден: {result == expected}\n")

#тест 2
print("Тест 2: a=5, b=5, f=9")
result = function_abf(5, 5, 9)
print(f"Результат: {result}")
print(f"Тест пройден: {result == 'a не должно быть равно b (деление на ноль)'}\n")

#тест 3
print("Тест 3: a=3, b=7, f=9")
result = function_abf(3, 7, 9)
print(f"Результат: {result}")
print(f"Тест пройден: {result == 'a-b должно быть больше 0 (для извлечения корня)'}\n")

#тест 4
print("Тест 4: a=10, b=6, f=-4")
result = function_abf(10, 6, -4)
print(f"Результат: {result}")
print(f"Тест пройден: {result == 'f должно быть больше 0 (для извлечения корня)'}\n")

#тест 5
print("Тест 5: a=6, b=2, f=0")
result = function_abf(6, 2, 0)
expected = ((6-2)**0.5/(6-2)) + 0**0.5
print(f"Результат: {result}")
print(f"Ожидалось: {expected}")
print(f"Тест пройден: {result == expected}\n")

#тест 6
print("Тест 6: a=100, b=96, f=25")
result = function_abf(100, 96, 25)
expected = ((100-96)**0.5/(100-96)) + 25**0.5
print(f"Результат: {result}")
print(f"Ожидалось: {expected}")
print(f"Тест пройден: {result == expected}\n")

#тест 7
print("Тест 7: a=2.5, b=0.5, f=4")
result = function_abf(2.5, 0.5, 4)
expected = ((2.5-0.5)**0.5/(2.5-0.5)) + 4**0.5
print(f"Результат: {result}")
print(f"Ожидалось: {expected}")
print(f"Тест пройден: {result == expected}\n")

#тест 8
print("Тест 8: Передача строки вместо числа")
try:
    result = function_abf("10", 6, 9)
    print(f"Результат: {result}")
    print("Тест пройден: False (Ожидалось исключение TypeError)\n")
except TypeError:
    print("Результат: Вызвано исключение TypeError")
    print("Тест пройден: True\n")

#тест 9
print("Тест 9: Большие числа")
result = function_abf(1000000000004, 1000000000000, 16)
expected = 4.5
print(f"Результат: {result}")
print(f"Тест пройден: {result == expected}")
