# Define the mixin classes
class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Implement the Dragon class inheriting from both mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Testing the Dragon's abilities
draco = Dragon()

draco.swim()  # Expected: "The creature swims!"
draco.fly()   # Expected: "The creature flies!"
draco.roar()  # Expected: "The dragon roars!"
