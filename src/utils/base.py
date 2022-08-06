import json
import sys
from data.classes import *


def read_json_file(filename: str):
    with open(filename) as f:
        config: dict[str, dict[str, dict]] = json.loads(f.read())
    return config


def str_to_class(classname: str) -> type:
    return getattr(sys.modules[__name__], classname)


def snake_to_pascal(table_name: str) -> str:
    """Название таблиц в snake_case, а классов в Pascal кейсе"""
    return table_name.replace("_", " ").title().replace(" ", "")
