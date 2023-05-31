# test_example.py
import pytest


def one_more(x):
    return x + 1


def test_correct():
    assert one_more(4) == 5


@pytest.mark.skip(reason="no way of currently testing this")
def test_fail():
    assert one_more(3) == 5


def get_sort_list(string):
    new_list = sorted(string.split(', '))
    return new_list


def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']
