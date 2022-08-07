import orjson
import sys
from data.classes import *
import re

PASCAL_TO_SNAKE_PATTERN = re.compile(r'(?<!^)(?=[A-Z])')


def read_json_file(filename: str):
    with open(filename, mode='r') as f:
        try:
            config_text = f.read()
            config: dict[str, dict[str, dict]] = orjson.loads(config_text)
        except FileNotFoundError:
            ...
    return config


def str_to_class(classname: str) -> type:
    return getattr(sys.modules[__name__], classname)


def snake_to_pascal(table_name: str) -> str:
    """Название таблиц в snake_case, а классов в Pascal кейсе"""
    return table_name.replace("_", " ").title().replace(" ", "")


def pascal_to_snake(table_name: str) -> str:
    """Название таблиц в snake_case, а классов в Pascal кейсе"""
    return PASCAL_TO_SNAKE_PATTERN.sub('_', table_name).lower()


def get_props(cls: type):
    return [getattr(cls, i) for i in cls.__dict__.keys() if not i.startswith('_')]
