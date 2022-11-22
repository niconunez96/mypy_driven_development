import random
from typing import Optional


class Book:
    def __init__(self, title: str):
        self._title = title

    def __str__(self) -> str:
        return f"Book[{self._title}]"

    def print(self) -> None:
        print(self)


def find_book() -> Book:
    if random.randint(1, 20) > 5:
        return None
    return Book("DDD")


"""
Types on mypy are `None` safety, we cannot assign a None to a type by default.
To allow `None` values we need the special type provided by typing module, called
`Optional`
"""


def find_book_opt() -> Optional[Book]:
    if random.randint(1, 20) > 5:
        return None
    return Book("DDD")


def main() -> None:
    book = find_book_opt()

    """
    mypy is smart here 🧠 and it knows that book can be a `None`
    So we cannot directly call book.print() because `None` do not have the method `print`
    """
    book.print()  # mypy complains ❌

    """
    To solve that issue we have to first check if book is not `None`
    This is call "type narrowing", when you check that the book is not `None` mypy discard
    that type "possibility" and now it knows that book can only be instance of Book
    """
    if not book:
        print("No book here 📚")
        return
    book.print()
