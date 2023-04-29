import pytest

def test_increment():
    def increment(n):
        return n + 1

    assert increment(3) == 4
# assert работает как if
# если True - идем дальше
# если False - AssertionError
# Запуск файла: pytest test_название файла.py

@pytest.mark.some_test
def test_a():
    assert True

@pytest.mark.some_test
def test_b():
    assert True
    
@pytest.mark.some_test
def test_c():
    assert True

'''
Пути:
1. pytest test_название файла.ру::название функции
2. Метка (@pytest.mark.название метки)
МЕТКА СОЗДАЕТСЯ ПЕРЕД ТЕСТОМ:
вызов метки: pytest название файла -m метка
'''

# Task - написать тест на функциональность по сложению чисел
@pytest.mark.calculate
def test_calculate():
    def calc(a, b):
        return a + b
    assert calc(2, 3) == 5

# skip - пропускает тест
# skipif - пропускает тест при определенных условиях
# parametrize - переиспользует тест с другими данными
@pytest.mark.new_version
@pytest.mark.skipif(
@pytest.mark.parametrize('number,number2', [[1, 2], [4, 6], [-1, 2], [0,0]])
def test_calculate_v2(number=None, number2=None):
    assert number + number2 > 0

'''
Homework 29.04
1. Почитать о служебных метках: https://docs.pytest.org/en/7.1.x/historical-notes.html#string-conditions
2. Написать тест, в котором будет проверка для ввода имени и фамилии
- Имя или Фамилия написаны с маленькой буквы (Пример: вася)
- Имя или фамилия написаны с большой буквы не в начале (Пример: вАся)
- Имя или фамилия начинаются не с цифр (Пример: 1Ваня)
3. Пароли. Написать тесты на проверку длины пароля
- Пароль должен быть минимум 8 и максимум 16 символов
- Пароль начинается с большой буквы и содержит буквы латиницы и числа
- Пароль не содержит символы (Пример: !?")

'''
