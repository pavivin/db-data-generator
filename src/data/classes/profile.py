from dataclasses import dataclass
from datetime import date, datetime

from .user import User


@dataclass(slots=True, frozen=True)
class Profile:
    profile_id: int
    name: str
    reg_date: date
