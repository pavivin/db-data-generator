from datetime import datetime
from utils.base_types import BaseStrTypeConfig

from utils.constants import OutputTypes
from utils import data_generator
from utils.models import TableBase, TableColumn

import json  # TODO: orjson

from data.generate_type import HINTING_TO_CLASSES

with open('src/data/statham.json') as f:
    config: dict[str, dict[str, dict]] = json.loads(f.read())


def _generate_columns(table: dict[str, dict]):
    columns = []
    for column_name, column in table.items():
        column_config = column['column_config']
        column_class = HINTING_TO_CLASSES[column_config['column_type']]
        values_select = column_config['values_select']
        table_column = TableColumn(
            column_name=column_name,
            column_config=column_class(BaseStrTypeConfig(values_select=values_select)),
        )
        columns.append(table_column)

    return columns


for tablename, table in config['tables'].items():
    tables = [
        TableBase(
            table_name=tablename,
            columns=_generate_columns(table),
        )
    ]

# table = TableBase(
#     table_name='people',
#     output_format=OutputTypes.CSV,
#     rows_to_generate=1000,
#     columns=[
#         TableColumn(
#             column_name='name',
#             column_config=base_types.BaseStrType(
#                 config=base_types.BaseStrTypeConfig(
#                     values_select=[
#                         base_types.ValuesFrequencyConfig(value='test1'),
#                         base_types.ValuesFrequencyConfig(value='test2'),
#                         base_types.ValuesFrequencyConfig(value='test3'),
#                     ]
#                 )
#             ),
#         ),
#         TableColumn(
#             column_name='int', column_config=base_types.BaseDecimalType(config=base_types.BaseDecimalTypeConfig())
#         ),
#         TableColumn(column_name='dec', column_config=base_types.BaseIntType(config=base_types.BaseIntTypeConfig())),
#         TableColumn(column_name='date', column_config=base_types.BaseDateType(config=base_types.BaseDateTypeConfig())),
#         TableColumn(
#             column_name='datetime',
#             column_config=base_types.BaseTimestampType(config=base_types.BaseTimestampTypeConfig()),
#         ),
#     ],
# )


generator = data_generator.TableDataGeneratorService(tables)
start_date = datetime.now()

generator.generate_table_data()

print(datetime.now() - start_date)
