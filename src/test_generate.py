from datetime import datetime

from utils.constants import OutputTypes
from utils import base_types, data_generator
from utils.models import TableBase, TableColumn

import json  # TODO: orjson

with open('src/data/statham.json') as f:
    config: dict[str, dict[str, dict]] = json.loads(f.read())

# for tablename, column in config['tables'].items():
#     [TableBase]
#     for column_name, column_config in column.items():
#         ...

table = TableBase(
    table_name='people',
    output_format=OutputTypes.CSV,
    rows_to_generate=1000,
    columns=[
        TableColumn(
            column_name='name',
            column_config=base_types.BaseStrType(
                config=base_types.BaseStrTypeConfig(
                    values_select=[
                        base_types.ValuesFrequencyConfig(value='test1'),
                        base_types.ValuesFrequencyConfig(value='test2'),
                        base_types.ValuesFrequencyConfig(value='test3'),
                    ]
                )
            ),
        ),
        TableColumn(
            column_name='int', column_config=base_types.BaseDecimalType(config=base_types.BaseDecimalTypeConfig())
        ),
        TableColumn(column_name='dec', column_config=base_types.BaseIntType(config=base_types.BaseIntTypeConfig())),
        TableColumn(column_name='date', column_config=base_types.BaseDateType(config=base_types.BaseDateTypeConfig())),
        TableColumn(
            column_name='datetime',
            column_config=base_types.BaseTimestampType(config=base_types.BaseTimestampTypeConfig()),
        ),
    ],
)


generator = data_generator.TableDataGeneratorService([table])
start_date = datetime.now()

generator.generate_table_data()

print(datetime.now() - start_date)
