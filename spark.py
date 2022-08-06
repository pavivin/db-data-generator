import os
from datetime import datetime, date

from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.storagelevel import StorageLevel

os.environ['PYSPARK_PYTHON'] = 'C:/Users/ichetverikov/Desktop/data-hack/data-hack/env/Scripts/python.exe'

spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

df = spark.createDataFrame(
    [
        Row(a=1, b=2.0, c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
        Row(a=2, b=3.0, c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
        Row(a=4, b=5.0, c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0)),
    ]
)

df.show()
df.persist(StorageLevel.DISK_ONLY)

parDF = spark.read.parquet("example2.parquet")
parDF.createOrReplaceTempView("ParquetTable")
spark.sql('select * from ParquetTable')

pass
