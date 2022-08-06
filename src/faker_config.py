from enum import Enum
from faker import Faker

from typing import NamedTuple

fake = Faker()


class StrFaker(Enum):
    name = 1


class FakerConfig(NamedTuple):
    str = StrFaker

