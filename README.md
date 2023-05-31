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