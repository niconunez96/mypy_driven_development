from dataclasses import dataclass
from datetime import datetime
from http import HTTPStatus
from typing import Literal, Tuple

from typing_extensions import assert_never

FailureMessage = Literal["NOT_FOUND", "INVALID_EVENT_STATUS", "INVALID_DATE"]


@dataclass(frozen=True)
class Failure:
    message: FailureMessage

    @property
    def to_http(self) -> HTTPStatus:
        match (self.message):
            case "NOT_FOUND":
                return HTTPStatus.NOT_FOUND
            case "INVALID_EVENT_STATUS" | "INVALID_DATE":
                return HTTPStatus.BAD_REQUEST
            case _:
                assert_never(self.message)


CommandResult = None | Failure


@dataclass(frozen=True)
class StartEventCommand:
    event_id: str
    start_date: datetime


def start_event(cmd: StartEventCommand) -> CommandResult:
    if cmd.start_date < datetime.now():
        return Failure("INVALID_DATE")
    if int(cmd.event_id) < 10:
        return Failure("NOT_FOUND")
    print("Starting event...")
    return None


class Success:
    pass


success = Success()


CommandResultV2 = Success | Failure


def start_event_2(cmd: StartEventCommand) -> CommandResultV2:
    if cmd.start_date < datetime.now():
        return Failure("INVALID_DATE")
    if int(cmd.event_id) < 10:
        return Failure("NOT_FOUND")
    print("Starting event...")
    return success


def endpoint(cmd: StartEventCommand) -> Tuple[int, str]:
    result = start_event(cmd)
    """
    Exhaustive checking does not work with complex objects.
    We are checking all available options but the assert never fails.
    """
    # match (result):
    #     case Failure("INVALID_DATE") | Failure("INVALID_EVENT_STATUS") as f:
    #         return 400, f.message
    #     case Failure("NOT_FOUND" as msg):
    #         return 404, msg
    #     case None:
    #         return 200, "Event started"
    #     case _:
    #         assert_never(result)
    match (result):
        case Failure(_) as f:
            return f.to_http, f.message
        case None:
            return HTTPStatus.OK, "Event started"
        case _:
            assert_never(result)


def endpoint_2(cmd: StartEventCommand) -> Tuple[HTTPStatus, str]:
    result = start_event_2(cmd)
    match (result):
        case Failure(_) as f:
            return f.to_http, f.message
        case Success():
            return HTTPStatus.OK, "Event started"
        case None:
            return HTTPStatus.OK, "Event started"  # mypy complains ❌
        case _:
            assert_never(result)
