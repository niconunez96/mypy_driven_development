from datetime import datetime


# Issue https://github.com/python/mypy/issues/12534
def is_my_birthday(date: datetime) -> bool:
    match (date):
        case birthday if birthday.day == datetime.now().day:
            return True
        case _:
            return False


def grocery(fruits: list[str]) -> None:
    """
    When we are doing pattern matching is VERY IMPORTANT THE ORDER
    As a general rule, more specific cases/patterns should go at first
    1. More Specific Cases ⬇️
    2. Less Specific Cases ⬇️
    3. Default Cases (wildcard) ⬇️
    """
    match (fruits):
        # case ["orange", *fruits]:  # This case is more general than the ones below
        #     print("Orange with more oranges or more fruits")
        case [*oranges] if all(orange == "orange" for orange in oranges):
            print(fruits)
            print("Box of oranges 📦🍊")
        case ["orange", *fruits] if "orange" not in fruits:
            print(fruits)
            print("Mix of fruits with first single orange 🍊🍌🍎🍍")
        case ["apple", _, "apple"]:
            print(fruits)
            print("x2 Apples and any fruit 🍎❓🍎")
        case ["banana", "banana", "banana"]:
            print(fruits)
            print("x3 Bananas 🍌🍌🍌")
        case _:
            print(fruits)
            print("I don't know what it is 🫠")
