from typing import Callable

from data.generate_type import CLASSES_TO_METHODS

from . import models

HINTING_TO_CLASSES = {}

class TableDataGeneratorService:
    """Сервис для генерации данных"""

    def __init__(self, config: models.TableBase, generate_type: dict[str, Callable] = CLASSES_TO_METHODS) -> None:
        self._config = config
        self._generate_type = generate_type

    def generate_table_data(self) -> None:
        """Генерация данных для таблицы"""
        result_data = ''

        for _ in range(self._config.rows_to_generate):  # TODO: потоки
            result_data += self._generate_row() + "\n"

        with open('kek.txt', 'w') as file:
            file.write(result_data)

    def _generate_row(self) -> str:
        row = ''

        for col in self._config.columns:
            row += self._generate_type[type(col.column_config)](col.column_config)
        return row
