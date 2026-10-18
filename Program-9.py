# PROGRAM 9 – Program to implement Polymorphism.

class Animal:
    """Base class providing a common interface."""
    def make_sound(self):
        pass

class Dog(Animal):
    """Subclass that overrides the parent method."""
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    """Subclass that overrides the parent method."""
    def make_sound(self):
        return "Meow!"

class Car:
    """An independent class with a matching method name."""
    def make_sound(self):
        return "Honk! Honk!"

def activate_sound(entity):

    """
    A single function that accepts any object (polymorphism).
    It calls the 'make_sound' method regardless of the object's class type.
    """

    print("{} says: {}".format(
        entity.__class__.__name__,
        entity.make_sound()
    ))

if __name__ == "__main__":

    dog = Dog()
    cat = Cat()
    car = Car()

    entities = [dog, cat, car]

    print("--- Testing Polymorphism ---")

    for item in entities:
        activate_sound(item)