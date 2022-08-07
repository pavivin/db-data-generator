from datetime import date, datetime
import pytest
from utils import base_types, data_generator
from utils.constants import OutputTypes

from utils.models import TableBase, TableColumn

# from src.utils import base_types

base_types.BaseStrType, base_types.BaseTimestampType, base_types.BaseDateType, base_types.Decimal, base_types.BaseIntType


@pytest.mark.parametrize(
    "column",
    [
        TableColumn(
            column_name='name',
            column_config=base_types.BaseStrType(values_select=[base_types.ValuesFrequency(value='test1')]),
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
def test_generate_date(column):
    table = TableBase(
        table_name='people',
        output_format=OutputTypes.CSV,
        rows_to_generate=10000,
        columns=[column],
    )
    generator = data_generator.TableDataGeneratorService([table])
    start_date = datetime.now()

    generator.generate_table_data()

    print(datetime.now() - start_date)
