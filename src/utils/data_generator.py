from json import dumps
from typing import Callable, Iterable

from data.generate_type import CLASSES_TO_METHODS

from . import constants, models


class TableDataGeneratorService:
    """Сервис для генерации данных"""

    def __init__(
        self, config: Iterable[models.TableBase], generate_type: dict[str, Callable] = CLASSES_TO_METHODS
    ) -> None:
        self._config_list = config
        self._generate_type = generate_type

    def generate_table_data(self) -> None:
        for config in self._config_list:
            self._generate_table_data(config)

    def _generate_table_data(self, config: models.TableBase) -> None:
        """Генерация данных для таблицы"""
        if config.output_format == constants.OutputTypes.JSON:
            work_func = self._generate_json_row

            result_data = f'[{self._generate_output(work_func=work_func, config=config)}]'

            for i in range(1, 7):
                if result_data[len(result_data) - i] == ',':
                    result_data = result_data[: len(result_data) - i] + result_data[len(result_data) - i + 1 :]
                    break

        elif config.output_format == constants.OutputTypes.CSV:

            work_func = self._generate_csv_row

            result_data = self._generate_csv_header(config)
            result_data += self._generate_output(work_func=work_func, config=config)

        with open(f'{config.table_name}.{config.output_format}', 'w') as file:
            file.write(result_data)

    def _generate_output(self, work_func: Callable, config: models.TableBase) -> str:
        """Генерация данных построчно"""
        result_data = ''
        for _ in range(config.rows_to_generate):  # TODO: потоки ?
            result_data += work_func(config) + '\n'

        return result_data

    def _generate_json_row(self, config: models.TableBase) -> dict:
        """Генерация json строки"""
        row = {
            col.column_name: self._generate_type[type(col.column_config)](col.column_config)
            for col in config.columns
        }

        return str(f'{dumps(row)},')

    def _generate_csv_header(self, config: models.TableBase) -> str:
        """Генерация шапки таблицы для csv"""
        header = '; '.join(col.column_name for col in config.columns)

        return f'{header}\n'

    def _generate_csv_row(self, config: models.TableBase) -> str:
        """Генерация csv строки"""
        row = '; '.join(
            [str(self._generate_type[type(col.column_config)](col.column_config)) for col in config.columns]
        )

        return row
