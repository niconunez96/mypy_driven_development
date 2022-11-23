from dataclasses import dataclass
from typing import NamedTuple, TypedDict


class EmailMessage(TypedDict):
    to: list[str]
    subject: str
    body: str


@dataclass(frozen=True)
class Failure:
    msg: str

    def __str__(self) -> str:
        return f"Failure[{self.msg}]"


class EmailUnsent(NamedTuple):
    to: list[str]
    message: EmailMessage
    failure: Failure
