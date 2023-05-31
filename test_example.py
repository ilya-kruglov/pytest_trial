# test_example.py
# import pytest


def one_more(x):
    return x + 1


def get_sort_list(string):
    new_list = sorted(string.split(', '))
    return new_list


def test_correct():
    print('Правильный тест')  # Новая строка.
    assert one_more(4) == 5


# @pytest.mark.skip(reason="no way of currently testing this")
def test_fail():
    print('Неправильный тест')  # Новая строка.
    assert one_more(3) == 5


def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']


def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    # Провальный тест:
    # ожидаем число, но вернётся список.
    assert isinstance(result, int)
