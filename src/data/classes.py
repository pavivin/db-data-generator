from dataclasses import dataclass

from faker import Faker

fake = Faker('en_US')


@dataclass(slots=True, frozen=True)
class Penis:
    penis_id: int
    name: str
    human_id: "Human"


@dataclass
class Human:
    human_id: int
    name: str
