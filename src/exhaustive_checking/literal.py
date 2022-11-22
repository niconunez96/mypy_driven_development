from typing import Literal

from typing_extensions import assert_never

Command = Literal["ProcessOrder", "SendEmail", "SendPushNotification"]


def execute_command(cmd: Command) -> None:
    if cmd == "ProcessOrder":
        print("Processing order📑...")
    elif cmd == "SendEmail":
        print("Sending email 📧...")


# What happen if we add a new command ?
# Is there a way mypy can help me ?
def execute_command_ex(cmd: Command) -> None:
    if cmd == "ProcessOrder":
        print("Processing order📑...")
    elif cmd == "SendEmail":
        print("Sending email 📧...")
    # elif cmd == "SendPushNotification":
    #     print("Sending push 📲...")
    else:
        assert_never(cmd)
