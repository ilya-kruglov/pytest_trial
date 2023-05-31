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