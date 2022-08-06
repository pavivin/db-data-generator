from utils import data_generator
from utils.models import TableBase, TableColumn
from utils import base_types


table = TableBase(
    table_name="people",
    rows_to_generate=1000,
    columns=[
        TableColumn(
            column_name="name",
            column_type=base_types.BaseStrType(
                config=base_types.BaseStrTypeConfig(
                    values_select=[
                        base_types.ValuesFrequencyConfig(value="test1"),
                        base_types.ValuesFrequencyConfig(value="test2"),
                        base_types.ValuesFrequencyConfig(value="test3"),
                    ]
                )
            ),
        ),
        TableColumn(column_name="value", column_type=base_types.BaseIntType(config=base_types.BaseIntTypeConfig())),
    ],
)


generator = data_generator.TableDataGeneratorService(table)

generator.generate_table_data()
