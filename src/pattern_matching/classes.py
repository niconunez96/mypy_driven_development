a: int | str = "asd"


def match_a() -> None:
    match (a):
        case int(value):
            print(f"Int with value: {value}")
        case str(value):
            print(f"Str with value: {value}")


def print_actions(actions: list[dict]) -> None:
    for action in actions:
        match action:
            case {"text": str(message), "color": str(c)}:
                print(f"ui.set_text_color({c})")
                print(f"ui.display({message})")
            case {"sleep": float(duration)}:
                print(f"ui.wait({duration})")
            case {"sound": str(url), "format": "ogg"}:
                print(f"ui.play({url})")
            case {"sound": _, "format": _}:
                print("warning('Unsupported audio format')")
