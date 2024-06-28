from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Subclass Dog
class Dog(Animal):
    def sound(self):
        return "Bark"

# Subclass Cat
class Cat(Animal):
    def sound(self):
        return "Meow"

# Example usage
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
