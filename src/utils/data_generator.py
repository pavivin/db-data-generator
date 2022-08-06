import random
import string
from datetime import date, datetime
from decimal import Decimal
from typing import Callable

from faker import Faker

from data.generate_type import CLASSES_TO_METHODS
from utils import base_types


from . import models


HINTING_TO_CLASSES = {}

class TableDataGeneratorService:
    """Сервис для генерации данных"""

    def __init__(self, config: models.TableBase, generate_type: dict[str, Callable] = CLASSES_TO_METHODS) -> None:
        self._config = config
        self._generate_type = generate_type

    def generate_table_data(self) -> None:
        """Генерация данных для таблицы"""
        result_data = ''

        for _ in range(self._config.rows_to_generate):  # TODO: потоки
            result_data += self._generate_row() + "\n"

        with open('kek.txt', 'w') as file:
            file.write(result_data)

    def _generate_row(self) -> str:
        row = ''

        for col in self._config.columns:
            row += self._generate_type[type(col.column_config)](col.column_config)
        return row

    @staticmethod
    def _generate_fake_str_data(row_config: base_types.BaseStrType) -> str:
        """Генерация строки по конфигурации"""
        config = row_config.config

        if config.faker_type:
            print('faker')
            pass  # TODO: генерация с помощью faker
            return

        elif config.values_select:
            selected_value = random.choice(config.values_select)
            return selected_value.value

        elif config.mask:
            generated_value = config.mask.replace(
                '#', random.choice(config.allowed_symbols if config.allowed_symbols else row_config.alphabet)
            )

            return generated_value

        else:
            return ''.join(
                random.choice(string.ascii_uppercase + string.digits)
                for _ in range(random.choice(range(config.min_length, config.max_length)))
            )

    @staticmethod
    def _generate_fake_int_data(row_config: base_types.BaseIntType) -> int:
        """Генерация целочисленного значения по конфигурации"""
        config = row_config.config

        if config.faker_type:
            print('faker')
            pass  # TODO: генерация с помощью faker
            return

        elif config.values_select:
            selected_value = random.choice(config.values_select)
            return selected_value.value

        elif config.mask:
            generated_value = config.mask.replace('#', random.choice(row_config.alphabet))
            return generated_value

        else:
            return random.choice(range(config.min_value, config.max_value))

    @staticmethod
    def _generate_fake_decimal_data(row_config: base_types.BaseDecimalType) -> Decimal:
        """Генерация дробного значения по конфигурации"""
        config = row_config.config

        if config.faker_type:
            print('faker')
            pass  # TODO: генерация с помощью faker
            return

        elif config.values_select:
            selected_value = random.choice(config.values_select)
            return selected_value.value

        elif config.mask:
            generated_value = config.mask.replace('#', random.choice(row_config.alphabet))
            return generated_value

        else:
            return random.choice(range(config.min_value, config.max_value))

    @staticmethod
    def _generate_fake_date_data(row_config: base_types.BaseDateType) -> date:
        """Генерация даты по конфигурации"""
        fake = Faker("en_US")
        config = row_config.config

        return fake.date_between(
            start_date=next(
                start_date for start_date in [config.start_date, date(1970, 1, 1)] if start_date is not None
            ),
            end_date=next(end_date for end_date in [config.end_date, date.today()] if end_date is not None),
        )

    @staticmethod
    def _generate_fake_timestamp_data(row_config: base_types.BaseTimestampType) -> datetime:
        """Генерация даты/времени по конфигурации"""
        fake = Faker("en_US")
        config = row_config.config

        return fake.date_time_between(
            start_date=next(
                start_date
                for start_date in [config.start_date, datetime(1970, 1, 1, 0, 0, 0)]
                if start_date is not None
            ),
            end_date=next(end_date for end_date in [config.end_date, datetime.today()] if end_date is not None),
        )


generate_type = {
    'str': TableDataGeneratorService._generate_fake_str_data,
    'datetime': TableDataGeneratorService._generate_fake_timestamp_data,
    'date': TableDataGeneratorService._generate_fake_date_data,
    'float': TableDataGeneratorService._generate_fake_decimal_data,
    'int': TableDataGeneratorService._generate_fake_int_data,
}
