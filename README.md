# pytest_trial

> pytest
> pytest -v
> pytest -vv

> pytest -q
> pytest -qq

> pytest file_name.py::TestClassName::test_method_name
> pytest file_name.py::TestClassName
> pytest file_name.py

> pytest test_example.py::test_fail
> pytest test_example.py::test_fail test_example.py::test_correct

> pytest pytest_trial
> pytest pytest_trial/test_example.py

> pytest -k "correct"
> pytest -k "not correct"
> pytest -k "(django or python) and not javascript"

#### Спринт 8/25 → Тема 5/8: Библиотека pytest → Урок 2/6

> pytest test_example.py -qq --lf
> pytest test_example.py -qq --ff
> pytest --ff -x
> pytest --ff --maxfail=2
> pytest --sw
> pytest --sw --stepwise-skip
> pytest test_example.py -qq --nf

#### Спринт 8/25 → Тема 5/8: Библиотека pytest → Урок 3/6

> pytest -k "correct or fail"
> pytest -s -k "correct or fail"
> pytest --capture=no -k "correct or fail"
> pytest -v -s -k "correct or fail"
> pytest -rP -k "correct or fail"
> pytest test_pdb.py -v -s
> pytest test_pdb.py -rP
> pytest test_pdb.py --trace --lf -x
> pytest test_pdb.py

```
n (next) — перейти к следующей строке текущей функции (если в текущей строке вызывается какая-то функция, то pdb не будет «проваливаться» в неё).
s (step) — перейти к следующей строке в текущей или в вызываемой функции.
j (jump) — перейти к указанному номеру строки. По коду можно передвигаться как вперёд, так и назад; есть ряд ограничений, рассмотрим их позже.
c (continue) — продолжить выполнение до следующей точки останова.
p (print) — напечатать значение переменной или выражения.
a (args) — напечатать аргументы текущей функции.
l (list) — вывести строки кода выполняемой программы.
q (quit) — выйти из режима отладки.
```

 ##### pdb.set_trace()
> pytest test_pdb.py --pdb

> pytest test_pdb.py --trace

#### Спринт 8/25 → Тема 5/8: Библиотека pytest → Урок 4/6

> pytest --markers

> import pytest
> Тест с этим маркером будет пропущен.
> @pytest.mark.skip

> import pytest
> Все тесты в этом файле будут пропущены.
> pytestmark = pytest.mark.skip

```
@pytest.mark.xfail("sys.version_info < (2, 1)", 
                   reason='Это старая версия Python, чего же вы ждали!')
def test_for_new_python():
    # Тест, который провалится на старых версиях Python.
    ... 
```
> pytest test_example.py::test_one_more -v

```
Сколько раз будет выполнен тест test_cartesian_product()?

def cartesian_product(a, b):
    return a * b


@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', ['one', 'two'])
def test_cartesian_product(x, y):
    assert cartesian_product(x, y) is not None 

Ответ: 4 раза. Маркеры можно комбинировать между собой. В приведённом коде тест будет выполнен столько раз, сколько есть сочетаний переданных аргументов.
```

#### Спринт 8/25 → Тема 5/8: Библиотека pytest → Урок 5/6
##### @pytest.fixture

```
@pytest.mark.usefixtures('one_fixture', 'another_fixture')
Обратите внимание, что такой способ работает только с тестирующими функциями. Если в одной фикстуре нужно вызвать другую — этот маркер не сработает!
```

> pytest test_engine.py -v
> pytest -s -qq test_engine.py

#### Спринт 8/25 → Тема 5/8: Библиотека pytest → Урок 6/6
##### conftest, pytest.ini

> pytest -m "slow"

```
# Запустить тесты, не отмеченные маркером slow:
pytest -m "not slow"
# Запустить тесты, отмеченные одновременно маркерами web и slow:
pytest -m "web and slow"
# Запустить тесты, отмеченные маркером web или slow:
pytest -m "web or slow"
```

```
# pytest.ini
[pytest]
python_files = check_*.py
python_classes = Check*
python_functions = *_check
```

> pytest -o minversion=6 -o addopts=-v

```
Отключение кеша настраивается так:
# pytest.ini
addopts = -p no:cacheprovider 
```

> pytest -o addopts=-vv

```
.pytest.ini (если имя файла начинается с точки, то в Linux этот файл будет скрыт);
pyproject.toml (универсальный файл настроек для проекта, может содержать в себе настройки разных инструментов, а не только pytest);
tox.ini (файл настроек для тестов, написанных при помощи библиотеки tox, но поддерживается и pytest);
setup.cfg (устаревший вариант, не рекомендуется к использованию).
```