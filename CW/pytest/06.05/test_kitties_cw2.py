# Фикстуры желательно писать в файле conftest.py
import pytest

# Как используется фикстура? Напиши ее имя в создании функции
# def имя функции(фикстура, параметры)
# Фикстур может быть много!
# Фикстура add_one срабатывает ПЕРЕД тестом
@pytest.mark.parametrize(('n', 'result'), [(1, 2), (2, 3)])
def test_add_one(add_one, n, result):
    one = add_one
    assert one + n == result

@pytest.mark.zero
def test_check_zero(check_zero):
    assert check_zero[1] and check_zero[0] == 0

@pytest.mark.yld
def test_check_yield(check_yield):
    some_text = ''
    some_text = check_yield
    assert some_text != ''


@pytest.mark.palindrome
def test_check_palindrome(generate_palindrome):
    assert generate_palindrome == generate_palindrome[::-1]

'''
HW 06.05
1. Почитать о фикстурах:
https://pytest-docs-ru.readthedocs.io/ru/latest/fixture.html
2. Решить задачу и написать на нее тесты
https://www.codewars.com/kata/62c93765cef6f10030dfa92b
3. Напишите фикстуру для задачи 2 и используйте ее.
'''
