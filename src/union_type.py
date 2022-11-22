# from typing import Union


class Book:
    def __init__(self, id: str, title: str) -> None:
        self.id = id
        self.title = title

    def print(self) -> None:
        return print(f"Book[{self.id}, {self.title}]")


class Failure:
    msg: str

    def __init__(self, msg: str) -> None:
        self.msg = msg


BookResult = Book | Failure
"""
For python versions < 3.10 we have to use this 👇🏼 syntax
"""
# Result = Union[Book, Failure]


def find_book(id: int) -> BookResult:
    """
    We can represent our use cases with more descriptive
    types, revealing intention in our APIs.
    Our `find_book` use case reveals that it can return either
    a `Book` or a `Failure` and it's revealed on the API itself!! 📜
    not adding a docstring specifying that we can raise a custom Exception
    """
    if id < 10:
        return Failure("Book was not found")
    return Book(str(id), "DDD")


def process_book(book: BookResult) -> None:
    if isinstance(book, Failure):
        print(f"Book was a failure 💥 - {book.msg}")
        return
    """
    The type narrowing again is helping us 🙏🏼
    """
    book.print()


def main() -> None:
    process_book(find_book(5))
    process_book(find_book(15))
