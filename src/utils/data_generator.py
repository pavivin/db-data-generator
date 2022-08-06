from json import dumps
from typing import Callable

from data.generate_type import CLASSES_TO_METHODS

from . import models
from . import constants

HINTING_TO_CLASSES = {}


class TableDataGeneratorService:
    """Сервис для генерации данных"""

    def __init__(self, config: models.TableBase, generate_type: dict[str, Callable] = CLASSES_TO_METHODS) -> None:
        self._config = config
        self._generate_type = generate_type

    def generate_table_data(self) -> None:
        """Генерация данных для таблицы"""
        if self._config.output_format == constants.OutputTypes.JSON:
            work_func = self._generate_json_row

            result_data = f'[{self._generate_output(work_func=work_func)}]'

            for i in range(1, 7):
                if result_data[len(result_data) - i] == ',':
                    result_data = result_data[: len(result_data) - i] + result_data[len(result_data) - i + 1 :]
                    break

        elif self._config.output_format == constants.OutputTypes.CSV:

            work_func = self._generate_csv_row

            result_data = self._generate_csv_header()
            result_data += self._generate_output(work_func=work_func)

        with open(f'{self._config.table_name}.{self._config.output_format}', 'w') as file:
            file.write(result_data)

    def _generate_output(self, work_func: Callable) -> str:
        """Генерация данных построчно"""
        result_data = ''
        for _ in range(self._config.rows_to_generate):  # TODO: потоки ?
            result_data += work_func() + '\n'

        return result_data

    def _generate_json_row(self) -> dict:
        """Генерация json строки"""
        row = {}

        for col in self._config.columns:
            row[col.column_name] = self._generate_type[type(col.column_config)](col.column_config)

        return str(f'{dumps(row)},')

    def _generate_csv_header(self) -> str:
        """Генерация шапки таблицы для csv"""
        header = '; '.join(col.column_name for col in self._config.columns)

        return f'{header[:-1]}\n'

    def _generate_csv_row(self) -> str:
        """Генерация csv строки"""
        row = '; '.join(
            [str(self._generate_type[type(col.column_config)](col.column_config)) for col in self._config.columns]
        )

        return row[:-1]
