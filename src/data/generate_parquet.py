import pandas as pd

import pyarrow as pa
import pyarrow.parquet as pq

from utils.constants import OutputTypes
from settings import OUTPUT_FOLDER


def generate_parquet(table_name: str, output_type: OutputTypes) -> None:
    """Генерация паркета на пол"""
    df = pd.read_csv(f'{OUTPUT_FOLDER}/{table_name}.{output_type}')
    table = pa.Table.from_pandas(df)

    pq.write_table(table, f'{OUTPUT_FOLDER}/{table_name}.parquet')
