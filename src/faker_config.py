from enum import Enum
from faker import Faker
fake = Faker()

class FakerConfig(str, Enum):
    'str': fake.weights