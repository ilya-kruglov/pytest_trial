# test_engine.py
import pytest

# Импортируем класс двигателя.
from .engine_class import Engine


@pytest.fixture
def engine():
    """Фикстура возвращает экземпляр класса двигателя."""
    return Engine()


# Эта фикстура не возвращает никаких значений, но изменяет объект,
# созданный другой фикстурой.
@pytest.fixture(autouse=True)  # Обозначаем фикстуру как автоматически вызываемую для всех тестов.
def start_engine(engine):  # Вызываем фикстуру получения объекта двигателя.
    """Фикстура запускает двигатель."""
    # Изменяем значение свойства объекта:
    engine.is_running = True


def test_engine_is_running(engine):
    """Тест проверяет, работает ли двигатель."""
    assert engine.is_running  # Проверяем, что значение атрибута is_running это True.
