import pandas as pd

import pyarrow as pa
import pyarrow.parquet as pq

from ..utils.constants import OutputTypes


def generate_parquet(table_name: str, type: OutputTypes) -> None:
    """Генерация паркета на пол"""
    df = pd.read_csv(f'{table_name}.{type}')
    table = pa.Table.from_pandas(df)

    pq.write_table(table, 'example2.parquet')
