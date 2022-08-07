import os

from pyspark.sql import SparkSession

from data.generate_parquet import generate_parquet
from utils.constants import OutputTypes

from settings import OUTPUT_FOLDER
os.environ['PYSPARK_PYTHON'] = 'C:/Users/ichetverikov/Desktop/data-hack/data-hack/env/Scripts/python.exe'


class SparkSessionService:
    """Сервис для работы с сессией spark"""

    def __init__(self) -> None:
        self.spark = SparkSession.builder.master("local[1]").appName("Spark").getOrCreate()

    def create_data_frame_from_parquet(self, table_name: str, output_type: OutputTypes) -> None:
        """Создание дата фрейма из паркета"""
        generate_parquet(table_name=table_name, output_type=output_type)

        parq = self.spark.read.parquet(f'{OUTPUT_FOLDER}/{table_name}.parquet')
        parq.createOrReplaceTempView(f'{table_name}')
        self.spark.sql(f'select * from {table_name}').show(1000, False)


# spark_session = SparkSessionService()
