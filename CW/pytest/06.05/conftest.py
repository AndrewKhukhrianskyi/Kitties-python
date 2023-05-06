# В этом файле будут лежать фикстуры
import pytest

from random import randint, choice

# Метка превращает функцию в фикстуру
@pytest.fixture()
def add_one():
    return 1

@pytest.fixture()
def check_zero():
    random_number = randint(0, 3)
    if random_number == 0:
        return random_number, True
    else:
        return random_number, False

# yield - умный return с паузой
# scope - это параметр запуска фикстуры
# Логика перед yield сработает ПЕРЕД тестом
# Логика после yield сработает ПОСЛЕ теста
@pytest.fixture(scope='module')
def check_yield():
    text = 'Before yield'
    yield text # сработает как return с паузой
    text = 'After yield'
    assert text == 'After yield'

@pytest.fixture()
def generate_palindrome():
    palindromes = ['мадам', 'козел', 'ведро']
    return choice(palindromes)




    
    
