from datetime import datetime
import time

from data.classes import all_dataclasses
from data.generate_type import HINTING_TO_CLASSES
from settings import JSON_CONFIG_PATH
from utils import base_types, data_generator
from utils.base import pascal_to_snake, read_json_file, str_to_class
from utils.constants import OutputTypes
from utils.models import TableBase, TableColumn

config = read_json_file(JSON_CONFIG_PATH)


def _generate_columns(table_name: str, table_class: type):
    columns = []
    json_table_data = config['tables'].get(table_name, {})
    for column_name, column_type in table_class.__annotations__.items():
        column_data = json_table_data.get(column_name)
        if column_data:
            columns.append(
                TableColumn(
                    column_name=column_name,
                    column_config=HINTING_TO_CLASSES[column_type.__name__](
                        values_select=[
                            base_types.ValuesFrequency(
                                value=item['values_frequency'].get('value'),
                                frequency=item['values_frequency'].get('frequency'),
                            )
                            for item in column_data['values_select']
                        ]
                    ),
                )
            )
    return columns


def generate_data():

    tables = []

    # class_name = имя класса (UserTest) - PascalCase
    # tablename = имя таблицы user_test - snake_case
    # можно настроить тип (snake_case, cebab_case, camelCase, PascalCase)

    for class_name in all_dataclasses:
        try:
            table_name = pascal_to_snake(class_name)
            table_class = str_to_class(class_name)
        except AttributeError as e:
            raise RuntimeError(f'Таблица {e.name} не найдена')

        rows_count = config['tables'].get(table_name, {'rows_count': 100}).get('rows_count')

        tables.append(
            TableBase(
                table_name=class_name,
                rows_to_generate=rows_count,
                output_format=config['output_format'],
                columns=_generate_columns(table_name, table_class),
            )
        )

    generator = data_generator.TableDataGeneratorService(tables)
    start_date = datetime.now()

    generator.generate_table_data()

    print(datetime.now() - start_date)

    print('INFO: press Enter to continue')
    time.sleep(120)


generate_data()
