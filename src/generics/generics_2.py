from typing import TypeVar

from src.generics.generics_1 import Animal, Box, Cat, Dog


def foo(animal: Box[Animal]) -> None:
    pass


# If we don't have access to the Box class to make it covariant
# We can use the upper bound approach
T = TypeVar("T", bound=Animal)


def make_animal_walk(box_animal: Box[T], default: T) -> None:
    # We cannot assign to the box either a cat or a dog because
    # mypy don't know the specific type inside the box, the most that it knows
    # is that it's something of type Animal but not which one.
    box_animal._value = Cat()  # mypy complains ❌
    # We cannot use a default of any type of Animal because of the same as
    # above.
    box_animal.get_value_or(Cat())  # mypy complains ❌
    box_animal.do(lambda animal: animal.walk())
    animal = box_animal.get_value_or(default)
    animal.walk()


def main() -> None:
    # We have already seen that this do not work
    box_cat = Box(Cat())
    box_dog = Box(Dog())
    # foo(box_cat)  # mypy complains ❌
    # foo(box_dog)  # mypy complains ❌

    # We know that it's a cat but mypy not
    make_animal_walk(box_cat, Cat())
    # foo2(box_cat, Dog()) # mypy complains ❌
    make_animal_walk(box_dog, Dog())
