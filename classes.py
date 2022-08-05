from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class Penis:
    penis_id: int
    name: str
    human_id: "Human"


@dataclass
class Human:
    human_id: int
    name: str
    age: int
    registration_date: datetime