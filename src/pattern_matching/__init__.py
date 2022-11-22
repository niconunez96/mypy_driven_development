from datetime import datetime, timedelta

from src.pattern_matching.classes import match_a, print_actions
from src.pattern_matching.conditionals import grocery, is_my_birthday
from src.pattern_matching.exhaustive_checking import (
    StartEventCommand,
    endpoint,
    endpoint_2,
)

# https://peps.python.org/pep-0636/#abstract


def main() -> None:

    print("Pattern matching with scalar types")
    match_a(10)
    match_a("something")
    print()

    print("Pattern matching with dictionaries")
    print_actions(
        [
            {"text": "foo", "color": "green"},
            {"sleep": 10.5},
            {"sound": "wave", "format": "ogg"},
            {"sound": "wave", "format": "mp3"},
        ]
    )
    print()

    print("Pattern matching with conditionals")
    print("Is my birthday", is_my_birthday(datetime.now()))
    print("Is my birthday", is_my_birthday(datetime.now() - timedelta(days=1)))
    print()
    grocery(["orange"])
    grocery(["orange", "orange", "orange"])
    grocery(["orange", "apple", "pineapple"])
    grocery(["banana", "banana", "banana"])
    grocery(["apple", "banana", "apple"])
    grocery(["apple", "orange", "apple"])
    grocery(["pineapple", "pineapple", "pineapple"])
    print()

    print("Pattern matching with exhaustive checking")
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
