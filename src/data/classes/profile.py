from dataclasses import dataclass

from .user import User


@dataclass(slots=True, frozen=True)
class Profile:
    profile_id: int
    name: str
    human_id: "User"
