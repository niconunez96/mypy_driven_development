from datetime import datetime

from src.pattern_matching.exhaustive_checking import (
    StartEventCommand,
    endpoint,
    endpoint_2,
)

# https://peps.python.org/pep-0636/#abstract


def main() -> None:
    start_event_cmd = StartEventCommand(event_id="1", start_date=datetime(2018, 12, 9))
    response = endpoint(start_event_cmd)
    print(response)
    response = endpoint_2(start_event_cmd)
    print(response)

    start_event_cmd = StartEventCommand(event_id="5", start_date=datetime(2025, 12, 9))
    response = endpoint(start_event_cmd)
    print(response)
    response = endpoint_2(start_event_cmd)
    print(response)

    start_event_cmd = StartEventCommand(event_id="15", start_date=datetime(2025, 12, 9))
    response = endpoint(start_event_cmd)
    print(response)
    response = endpoint_2(start_event_cmd)
    print(response)
