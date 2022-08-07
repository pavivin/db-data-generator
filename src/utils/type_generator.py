import datetime
import random
import string
from datetime import date, datetime
from decimal import Decimal

from faker import Faker

from utils import base_types

fake = Faker("en_US")


class TypeGenerator:
    @staticmethod
    def generate_fake_str_data(row_config: base_types.BaseStrType) -> str:
        """Генерация строки по конфигурации"""
        if row_config.faker_type:
            pass  # TODO: генерация с помощью faker
            return

        elif row_config.values_select:
            selected_value = random.choice(row_config.values_select)
            return selected_value.value

        elif row_config.mask:
            generated_value = row_config.mask.replace(
                '#', random.choice(row_config.allowed_symbols if row_config.allowed_symbols else row_config.alphabet)
            )

            return generated_value

        else:
            return ''.join(
                random.choice(string.ascii_uppercase + string.digits)
                for _ in range(random.choice(range(row_config.min_length, row_config.max_length)))
            )

    @staticmethod
    def generate_fake_int_data(row_config: base_types.BaseIntType) -> int:
        """Генерация целочисленного значения по конфигурации"""

        if row_config.faker_type:
            pass  # TODO: генерация с помощью faker
            return

        elif row_config.values_select:
            selected_value = random.choice(row_config.values_select)
            return selected_value.value

        elif row_config.mask:
            generated_value = row_config.mask.replace('#', random.choice(row_config.alphabet))
            return generated_value

        else:
            return random.choice(range(row_config.min_value, row_config.max_value))

    @staticmethod
    def generate_fake_decimal_data(row_config: base_types.BaseDecimalType) -> Decimal:
        """Генерация дробного значения по конфигурации"""

        if row_config.faker_type:
            pass  # TODO: генерация с помощью faker
            return

        elif row_config.values_select:
            selected_value = random.choice(row_config.values_select)
            return str(selected_value.value)

        elif row_config.mask:
            generated_value = row_config.mask.replace('#', random.choice(row_config.alphabet))
            return str(generated_value)

        else:
            return str(Decimal(random.randrange(155, 389)) / 100)

    @staticmethod
    def generate_fake_date_data(row_config: base_types.BaseDateType) -> date:
        """Генерация даты по конфигурации"""

        return fake.date_between(
            start_date=next(
                start_date for start_date in [row_config.start_date, date(1970, 1, 1)] if start_date is not None
            ),
            end_date=next(end_date for end_date in [row_config.end_date, date.today()] if end_date is not None),
        ).isoformat()

    @staticmethod
    def generate_fake_timestamp_data(row_config: base_types.BaseTimestampType) -> datetime:
        """Генерация даты/времени по конфигурации"""
        return fake.date_time_between(
            start_date=next(
                start_date
                for start_date in [row_config.start_date, datetime(1970, 1, 1, 0, 0, 0)]
                if start_date is not None
            ),
            end_date=next(end_date for end_date in [row_config.end_date, datetime.today()] if end_date is not None),
        ).isoformat()
