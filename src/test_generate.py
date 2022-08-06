from utils import base_types, data_generator
from utils.models import TableBase, TableColumn


table = TableBase(
    table_name='people',
    rows_to_generate=1000,
    columns=[
        TableColumn(
            column_name='name',
            column_config=base_types.BaseStrType(
                config=base_types.BaseStrTypeConfig(
                    values_select=[
                        base_types.ValuesFrequencyConfig(
                            value='test1'
                        ),
                        base_types.ValuesFrequencyConfig(
                            value='test2'
                        ),
                        base_types.ValuesFrequencyConfig(
                            value='test3'
                        ),
                    ]
                )
            )
        )
    ]
)


generator = data_generator.TableDataGeneratorService(table)

generator.generate_table_data()
