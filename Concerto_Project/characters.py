from abc import ABC, abstractmethod
from random import randint

class Character(ABC):  # Make Character an abstract class
    """In this solution, the Character class has been transformed into an
    abstract class by using the ABC class.
    An abstract method named perform_action has been declared in the
    Character class. The Suspect and Witness subclasses then implement this
    abstract method with specific actions that demonstrate polymorphism. """

    def __init__(self):
        # Even in abstract classes we see encapsulation  as before.
        self.option = []
        self.name = ["Madoka", "Hugo", "Morgan", "Billy", "Renee", "Boots", "Mike Wazowski", "Big Guy", "Homura",
                     "Stinky Man", "Homeless Person", "Mike Tyson", "Toji", "Saitama"]

    def coffee_option(self, name):
        #choice = randint(1, 5)

        #if choice == 1:
            print(f"{name}: I would like a medium sized, hot coffee without milk and 3 sugars.\nPlease no ice\n")
            self.option = ["c", "m", "n", "3", "hot", "n"]

