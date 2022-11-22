from typing_extensions import assert_never
from enum import Enum


class OrderStatus(Enum):
    PENDING = 0
    ACTIVE = 1
    CANCELLED = 2
    DELIVERED = 3


class Order:
    _status: OrderStatus

    def __init__(self, status: OrderStatus) -> None:
        self._status = status

    def process(self) -> None:
        if self._status == OrderStatus.ACTIVE:
            print("Process ACTIVE")
        elif self._status == OrderStatus.PENDING:
            print("Process PENDING")
        elif self._status == OrderStatus.CANCELLED:
            print("Process CANCELLED")

    # What happen if we add a new status to process ?
    # Is there a way mypy can help me ?
    def process_ex(self) -> None:
        if self._status is OrderStatus.ACTIVE:
            print("Process ACTIVE")
        elif self._status is OrderStatus.PENDING:
            print("Process PENDING")
        elif self._status is OrderStatus.CANCELLED:
            print("Process CANCELLED")
        elif self._status is OrderStatus.DELIVERED:
            print("Process DELIVERED")
        else:
            print("Apparently assert never fails at runtime 🫠")
            assert_never(self._status)
