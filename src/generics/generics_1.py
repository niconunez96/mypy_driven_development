from dataclasses import dataclass
from typing import Callable, Generic, Optional, TypeVar

T = TypeVar("T")


class Box(Generic[T]):
    """
    Box is a "type constructor"
    We can create new types from it, i.e:
    * `Box[str]`
    * `Box[int]`
    * `Box[boolean]`
    """

    _value: Optional[T]

    def __init__(self, value: Optional[T] = None):
        self._value = value

    def __str__(self) -> str:
        return f"Box[{self._value}]"

    def do(self, f: Callable[[T], None]) -> None:
        if self._value:
            f(self._value)

    def get_value_or(self, default: T) -> T:
        return default if not self._value else self._value


class Animal:
    def walk(self) -> None:
        print("Walking... 👣👣👣")


class Dog(Animal):
    def __str__(self) -> str:
        return "DOG 🐶"

    def bark(self) -> None:
        print("Guau Guau 🐕")


class Cat(Animal):
    def __str__(self) -> str:
        return "CAT 😼"

    def meow(self) -> None:
        print("Meow Meow Meow 🐈")


def mutate_animal(box_animal: Box[Animal]) -> None:
    box_animal._value = Cat()


# How can we make our Box class covariant ?
TCov = TypeVar("TCov", covariant=True)


@dataclass(frozen=True)
class BoxCov(Generic[TCov]):
    """
    Box is a "type constructor"
    We can create new types from it, i.e:
    * `Box[str]`
    * `Box[int]`
    * `Box[boolean]`
    """

    _value: Optional[TCov]

    def __str__(self) -> str:
        return f"Box[{self._value}]"

    def do(self, f: Callable[[TCov], None]) -> None:
        if self._value:
            f(self._value)

    def get_value_or(self, default: TCov) -> TCov:  # type: ignore
        return default if not self._value else self._value


def make_animal_walk(box_animal: BoxCov[Animal]) -> None:
    box_animal.do(lambda animal: animal.walk())


def main() -> None:
    # We cannot instantiate a Box without providing a new type
    # box = Box()
    word = Box("something")
    non_word = Box[str]()
    print("*" * 20)
    print(word.get_value_or("default"))
    print(non_word.get_value_or("default"))
    print("*" * 20)

    print("*" * 20)
    print("INVARIANT BOX")
    box_dog = Box(Dog())
    """
    We cannot pass a Box[dog] because our foo function expect a Box[Animal]
    Generics by default are not "covariant" because by default objects are mutable
    This means that besides Dog inherits from Animal, then Box[dog] do not inherit from Box[Animal]
    """
    print("Now I'm a dog")
    print(box_dog)
    mutate_animal(box_dog)  # mypy complains ❌
    """
    foo function change the box that contains our dog but we didn't notice, fortunately mypy already warn us 🙌
    box_dog.do(lambda dog: dog.bark()) # <-- this will 💣
    """
    print("Now I'm a dog??, damn 'mutate_animal' transform my dog into a cat!!")
    print(box_dog)
    print("*" * 20)

    print("*" * 20)
    print("COVARIANT BOX")
    box_dog2 = BoxCov(Dog())
    make_animal_walk(box_dog2)
    box_dog2.do(lambda dog: dog.bark())
    print(box_dog2)
    print("*" * 20)
