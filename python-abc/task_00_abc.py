#!/usr/bin/python3
"""
class of Animal
"""
from abc import ABC, abstractmethod


class Animal():
    """An abstract base class representing animals.

    This class serves as a blueprint for defining
    common characteristics and behaviors of various
    animal species. It cannot be instantiated
    directly, but subclasses must inherit from it and
    implement the abstract
    `sound` method.

    Attributes:
        (None: abstract classes typically don't define
        attributes)

    Methods:
        sound(self) -> str (abstract):
            Raises a `TypeError` as this method is abstract
            and must be
            implemented by subclasses to return the
            characteristic sound of a specific animal.
    """
    @abstractmethod
    def sound(self):
        raise (TypeError("Can't instantiate abstract class\
                          Animal with abstract method sound"))


class Cat(Animal):
    """Returns the characteristic sound a Cat makes.

    Returns:
        str: The sound a Cat makes, which is "Meow".
    """
    def sound(self):
        return ("Meow")


class Dog(Animal):
    """Returns the characteristic sound a dog makes.

    Returns:
        str: The sound a dog makes, which is "Bark".
    """
    def sound(self):
        return ("Bark")
