from json import dumps
from typing import Callable, Iterable

from data.generate_type import CLASSES_TO_METHODS
from settings import OUTPUT_FOLDER

from . import constants, models
from spark.init_spark import SparkSessionService


class TableDataGeneratorService:
    """Сервис для генерации данных"""

    def __init__(
        self, config: Iterable[models.TableBase], generate_type: dict[str, Callable] = CLASSES_TO_METHODS
    ) -> None:
        self._config_list = config
        self._generate_type = generate_type
        self._spark_session = SparkSessionService()

    def generate_table_data(self, is_spark=True, output_folder: str = OUTPUT_FOLDER) -> None:
        for config in self._config_list:
            self._generate_table_data(config, is_spark, output_folder)

    def _generate_table_data(self, config: models.TableBase, is_spark=True, output_folder: str = OUTPUT_FOLDER) -> None:
        """Генерация данных для таблицы"""
        if config.output_format == constants.OutputTypes.JSON:
            work_func = self._generate_json_row

            result_data = f'[{self._generate_output(work_func=work_func, config=config)}]'

            for i in range(1, 7):
                if result_data[len(result_data) - i] == ',':
                    result_data = result_data[:len(result_data) - i] + result_data[len(result_data) - i + 1 :]
                    break

        elif config.output_format == constants.OutputTypes.CSV:

            work_func = self._generate_csv_row

            result_data = self._generate_csv_header(config)
            result_data += self._generate_output(work_func=work_func, config=config)

        else:
            raise RuntimeError(
                f'Некорректный тип вывода: {config.output_format}, корректные: {constants.OutputTypes.__dict__}'
            )

        with open(f'{output_folder}/{config.table_name}.{config.output_format}', 'w') as file:
            file.write(result_data)

        if is_spark:
            self._spark_session.create_data_frame_from_parquet(
                table_name=config.table_name, output_type=config.output_format
            )

    def _generate_output(self, work_func: Callable, config: models.TableBase) -> str:
        """Генерация данных построчно"""
        result_data = ''
        for _ in range(config.rows_to_generate):  # TODO: потоки ?
            result_data += work_func(config) + '\n'

        return result_data

    def _generate_json_row(self, config: models.TableBase) -> dict:
        """Генерация json строки"""
        row = {
            col.column_name: self._generate_type[type(col.column_config)](col.column_config) for col in config.columns
        }

        return str(f'{dumps(row)},')

    def _generate_csv_header(self, config: models.TableBase) -> str:
        """Генерация шапки таблицы для csv"""
        header = '; '.join(col.column_name for col in config.columns)

        return f'{header}\n'

    def _generate_csv_row(self, config: models.TableBase) -> str:
        """Генерация csv строки"""
        row = '; '.join(
            [str(self._generate_type[type(col.column_config)]()) for col in config.columns]
        )

        return row
