from typing import Any
from dataclasses import dataclass
from datetime import datetime


@dataclass()
class CreateEventCommand:
    name: str
    description: str
    owner_id: str


@dataclass(frozen=True)
class StartEventCommand:
    event_id: str
    start_date: datetime


@dataclass(frozen=True)
class EmailAddress:
    value: str

    """
    We cannot assign `value` either in the __init__ method
    How can we validate the value introduced in our Email ?
    """
    # def __init__(self, value: str) -> None:
    #     self.value = value

    def __post_init__(self, *args: Any) -> None:
        print(args)
        self.validate()

    def validate(self) -> None:
        assert "@" in self.value, "Invalid Email 📧, missing @"
        assert ".com" in self.value, "Invalid Email 📧, missing .com"


def main() -> None:
    """
    Dataclasses by default:
    1. Give default constructor for all of our attributes
    2. Make our dataclasses "equal" by its attributes
    3. Creates a __repr__ by its attributes
    """
    create_event_cmd = CreateEventCommand("Awesome event", "Some description", "1008")
    create_event_cmd_2 = CreateEventCommand("Awesome event", "Some description", "1008")

    print(
        f"""
    1. Dataclasses creates str representations of our classes
    2. Different instances are equal if they have the same value in their attributes 👬🏼
    {create_event_cmd} is equal to {create_event_cmd_2}
    result: {create_event_cmd == create_event_cmd_2}
    """
    )

    print(
        """
    With `frozen=True` all of the attributes of our dataclasses are immutable
    """
    )
    start_event_cmd = StartEventCommand("12", datetime(2018, 12, 9))
    start_event_cmd.event_id = "13"  # mypy complains ❌
    print(start_event_cmd)
    print()

    print(
        """
    Validate our Value Objects with `dataclass` using __post_init__
    """
    )
    EmailAddress("invalid@")  # <-- invalid email 💥
    EmailAddress("invalidemail.com")  # <-- invalid email 💥
    email = EmailAddress("valid@mail.com")
    print(email)
