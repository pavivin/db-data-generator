from datetime import datetime


from data.generate_type import HINTING_TO_CLASSES
from settings import JSON_CONFIG_PATH
from utils import base_types, data_generator
from utils.base import read_json_file, snake_to_pascal, str_to_class
from utils.constants import OutputTypes
from utils.models import TableBase, TableColumn


def _generate_columns(table: dict[str, dict], column_class: str):
    columns = []
    for column_name, column in table.items():
        if column_name != 'rows_count':
            column_class = HINTING_TO_CLASSES[table_class.__annotations__[column_name].__name__]
            values_select = column['values_select']
            table_column = TableColumn(
                column_name=column_name,
                column_config=column_class(
                    values_select=[
                        base_types.ValuesFrequency(
                            value=item['values_frequency']['value'],
                            frequency=item['values_frequency'].get('frequency'),
                        )
                        for item in values_select
                    ]
                ),
            )
            columns.append(table_column)

    return columns


config = read_json_file(JSON_CONFIG_PATH)
tables = []
for table_name, table in config['tables'].items():
    class_name = snake_to_pascal(table_name)
    try:
        table_class = str_to_class(class_name)
    except AttributeError as e:
        raise RuntimeError(f'Таблица {e.name} не найдена')
    tables.append(
        TableBase(
            table_name=table_name,
            rows_to_generate=table['rows_count'],
            output_format=OutputTypes.CSV,
            columns=_generate_columns(table, table_name),
        )
    )


generator = data_generator.TableDataGeneratorService(tables)
start_date = datetime.now()

generator.generate_table_data()

print(datetime.now() - start_date)

print('INFO: press Enter to continue')
input()
