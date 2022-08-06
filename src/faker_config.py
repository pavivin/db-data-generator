from enum import Enum
from typing import NamedTuple

from faker import Faker

fake = Faker()


class StrFaker(Enum):
    name = 1


class FakerConfig(NamedTuple):
    str = StrFaker

