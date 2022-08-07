from dataclasses import dataclass
from datetime import date


@dataclass(slots=True, frozen=True)
class Profile:
    profile_id: int
    name: str
    reg_date: date
