from datetime import datetime
from typing import Final, Literal, Optional

EventStatus = Literal["ACTIVE", "PENDING"]


class Event:
    id: Final[str]
    start_date: Optional[datetime] = None
    status: Final[EventStatus]

    def __init__(self, id: str, status: EventStatus, start_date: datetime = None):
        self.id = id
        self.status = status
        self.start_date = start_date

    def __str__(self) -> str:
        return f"Event[{self.id}, {self.status}, {self.start_date}]"

    @staticmethod
    def new_event(id: str) -> "Event":
        return Event(id, "PENDING")

    def start_event(self, start_date: datetime) -> "Event":
        """
        We cannot modify a final attributes
        This check is ignored at runtime ⏱️
        """
        self.status = "ACTIVE"  # mypy complains ❌
        self.start_date = start_date
        return Event(self.id, "ACTIVE", start_date)


def main() -> None:
    event = Event.new_event("5")
    print(event)
    started_event = event.start_event(datetime(2018, 12, 9))
    print(started_event)
