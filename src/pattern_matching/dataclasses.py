from dataclasses import dataclass
from typing import Literal


@dataclass
class Event:
    name: str
    status: Literal["ACTIVE", "DRAFT"]

    def __str__(self) -> str:
        return f"Event[{self.name}, {self.status}]"


def print_event(event: Event) -> None:
    match (event):
        case Event(_, "ACTIVE"):
            print("ACTIVE EVENT", event)
        case Event(_, "DRAFT"):
            print("DRAFT EVENT", event)
