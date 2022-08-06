# data-hack

## Debug со spark

1. Поставить точку останова в конце main.py
2. Как дойдет до конца можно выполнять все запросы в spark, пример:

```python
from spark.init_spark import spark_session


spark_session.spark.sql(f'select * from {table_name}').show(1000, False)
```

## Spark

Web ui: `127.0.0.1:4040`
