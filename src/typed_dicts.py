from dataclasses import dataclass
from typing import Any, TypedDict
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Password:
    value: str

    def __post_init__(self, *args: Any) -> None:
        self.validate()

    def validate(self) -> None:
        assert len(self.value) > 10, "Password must be greater than 10 💣"


@dataclass(frozen=True)
class UserId:
    value: UUID

    @staticmethod
    def from_string(id: str) -> "UserId":
        return UserId(UUID(id))


class UserResponse(TypedDict):
    id: str
    username: str
    password: str

    def show(self) -> None:
        """
        We cannot add methods to typed dicts
        """
        print(self)


class User:
    id: UserId
    username: str
    password: Password

    def __init__(self, id: UserId, username: str, password: Password) -> None:
        self.id = id
        self.username = username
        self.password = password

    def to_response(self) -> UserResponse:
        return {
            "id": str(self.id.value),
            "username": self.username,
            "password": self.password.value,
        }


def main() -> None:
    user = User(UserId(uuid4()), "nn", Password("somethingelse10"))
    user_response = user.to_response()

    print(user_response)
