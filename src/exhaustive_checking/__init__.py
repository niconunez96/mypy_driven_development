from src.exhaustive_checking.enum import Order, OrderStatus
from src.exhaustive_checking.literal import execute_command, execute_command_ex
from src.exhaustive_checking.union import BookById, UserById, query_bus


def main() -> None:
    active_order = Order(OrderStatus.DELIVERED)
    active_order.process()
    active_order.process_ex()

    execute_command("SendPushNotification")
    execute_command_ex("SendPushNotification")

    query_bus(UserById("1"))
    query_bus(BookById("1", "DDD"))
