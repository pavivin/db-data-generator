from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Penis:
    penis_id: int
    name: str
    human_id: "Human"


@dataclass
class Human:
    human_id: int
    name: str