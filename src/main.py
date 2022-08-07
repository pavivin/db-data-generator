from datetime import date, datetime

from data.classes import all_dataclasses
from data.generate_type import HINTING_TO_CLASSES
from settings import JSON_CONFIG_PATH
from utils import base_types, data_generator
from utils.base import pascal_to_snake, read_json_file, str_to_class
from utils.constants import OutputTypes
from utils.models import TableBase, TableColumn

config = read_json_file(JSON_CONFIG_PATH)


test_table_all_features = TableBase(
    table_name='people',
    output_format=OutputTypes.CSV,
    rows_to_generate=10000,
    columns=[
        TableColumn(
            column_name='name',
            column_config=base_types.BaseStrType(
                values_select=[
                    base_types.ValuesFrequency(value='test1'),
                    base_types.ValuesFrequency(value='test2'),
                    base_types.ValuesFrequency(value='test3'),
                ]
            ),
        ),
        TableColumn(column_name='int', column_config=base_types.BaseDecimalType()),
        TableColumn(column_name='dec', column_config=base_types.BaseIntType()),
        TableColumn(
            column_name='date',
            column_config=base_types.BaseDateType(start_date=date(2020, 1, 1), end_date=date(2022, 1, 1)),
        ),
        TableColumn(
            column_name='datetime',
            column_config=base_types.BaseTimestampType(),
        ),
    ],
)


def _generate_columns(table_name: str, table_class: type):
    columns = []
    json_table_data = config['tables'].get(table_name, {})
    for column_name, column_type in table_class.__annotations__.items():
        column_data = json_table_data.get(column_name)

        column_ = TableColumn(
            column_name=column_name,
            column_config=HINTING_TO_CLASSES[column_type.__name__](),
        )

        if column_data:

            if 'values_select' in column_data:
                column_.column_config.values_select = [
                    base_types.ValuesFrequency(
                        value=item['values_frequency'].get('value'),
                        frequency=item['values_frequency'].get('frequency'),
                    )
                    for item in column_data['values_select']
                ]

            if 'allowed_symbols' in column_data:
                column_.column_config.allowed_symbols = column_data['allowed_symbols']

            if 'mask' in column_data:
                column_.column_config.mask = column_data['mask']

            if 'min_length' in column_data:
                column_.column_config.min_length = column_data['min_length']

            if 'max_length' in column_data:
                column_.column_config.max_length = column_data['max_length']

            if 'min_fraction_numbers' in column_data:
                column_.column_config.min_fraction_numbers = column_data['min_fraction_numbers']

            if 'max_fraction_numbers' in column_data:
                column_.column_config.max_fraction_numbers = column_data['max_fraction_numbers']

            if 'start_date' in column_data:
                column_.column_config.start_date = datetime.strptime(column_data['start_date'], '%Y/%m/%d')

            if 'end_date' in column_data:
                column_.column_config.end_date = datetime.strptime(column_data['end_date'], '%Y/%m/%d')

        columns.append(column_)

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
    input()


generate_data()
