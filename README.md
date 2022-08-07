# data-hack

## Debug со spark

1. Поставить точку останова в конце main.py
2. Как дойдет до конца можно выполнять все запросы в spark, пример:

```python
from spark.init_spark import spark_session


spark_session.spark.sql(f'select * from {table_name}').show(1000, False)
```

## Spark

Web ui: `127.0.0.1:4040`

# Структура проекта

src/data/classes - папка с датаклассами

src/data/config.json - конфиг-файл для данных в датаклассах

data/output - выходные данные в виде JSON / CSV и parquet

src/main.py - запуск проекта

# Заполнение данных

## config.json

```json
{
  "output_format": "json", // выходной формат - json / csv
  "tables": {
    // таблицы
    "user": {
      // название таблицы
      "rows_count": 1000, // количество генерируемых строк
      "name": { // название колонки
        "values_select": [
          // массив возможных значений
          {
            "values_frequency": {
              "value": "test", // значение
              "frequency": 100 // частота
            }
          }
        ]
      },
      "user_id": {
        "values_select": [
          {
            "values_frequency": {
              "value": "test"
            }
          }
        ]
      }
    }
  }
}
```
## Датаклассы

Датаклассы соотносятся с названием в json через преоразование snake_case в json в PascalCase в названии класса

например: test_name (config.json) -> TestName (classes/test_name.py) 

```python
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class User:
    user_id: int
    name: str
```
Чтобы обращение по датаклассам было быстрее можно использовать атрибут slots
```python
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class User:
    user_id: int
    name: str
```

## Запуск (Python)
```bash
python -m venv env
source env/bin/activate (Linux)
env/bin/activate.ps1 (Windows)
pip install requirements.min.txt
python main.py
```

## Запуск (Docker)

```bash
docker build -t data-hack:latest .
```

## Запуск тестов

```bash
python -m pytest tests/
# или
env/bin/python -m pytest tests/
```