from datetime import datetime


# Issue https://github.com/python/mypy/issues/12534
def is_my_birthday(date: datetime) -> bool:
    match (date):
        case birthday if birthday == datetime.now():
            return True
        case _:
            return False
