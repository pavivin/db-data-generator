import os

from pyspark.sql import SparkSession

from ..data.generate_parquet import generate_parquet
from ..utils.constants import OutputTypes


os.environ['PYSPARK_PYTHON'] = 'C:/Users/ichetverikov/Desktop/data-hack/data-hack/env/Scripts/python.exe'


class SparkSessionService:
    """Сервис для работы с сессией spark"""

    def __init__(self) -> None:
        self.spark = SparkSession.builder.master("local[1]").appName("Spark").getOrCreate()

    @classmethod
    def create_data_frame_from_parquet(cls, table_name: str, type: OutputTypes) -> None:
        """Создание дата фрейма из паркета"""
        generate_parquet(table_name=table_name, type=type)

        parq = cls.spark.read.parquet(f'{table_name}.parquet')
        parq.createOrReplaceTempView(f'{table_name}')
        cls.spark.sql(f'select * from {table_name}').show(1000, False)

        print('INFO: press Enter to continue')
        input()
