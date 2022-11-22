from dataclasses import dataclass

from typing_extensions import assert_never


@dataclass(frozen=True)
class UserById:
    id: str


@dataclass(frozen=True)
class BookById:
    id: str
    name: str


Query = UserById | BookById


def query_bus(query: Query) -> dict:
    if isinstance(query, UserById):
        print(f"Finding user by id {query.id}")
        return {}
    # elif isinstance(query, BookById):
    #     print(f"Finding book by id {query.id} - {query.name}")
    #     return {}
    else:
        assert_never(query)
