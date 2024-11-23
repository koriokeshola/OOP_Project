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

    # @abstractmethod
    def perform_action(self, name):
        pass

    def coffee_option(self, name):
        choice = randint(1, 5)

        if choice == 1:
            print(f"{name}: I would like a medium sized, hot coffee without milk and 3 sugars.\nPlease no ice\n")
            self.option = ["c", "m", "n", "3", "hot", "n"]
        if choice == 2:
            print(f"{name}: I want a large hot coffee, add some milk, dont make it sweet. \nForget the ice\n")
            self.option = ["c", "l", "y", "0", "hot", "n"]
        if choice == 3:
            #cutie customer
            print(f"{name}: MORNING, I'd like a medium ice cold coffee, with alot of milk. \nAlot of sugar please!!\n")
            self.option = ["c", "m", "y", "3", "cold", "y"]
        if choice == 4:
            print(f"{name}: Can I get a small coffee with not much sugar, no ice, and add milk. \nOh and make it really hot\n")
            self.option = ["c", "s", "y", "1", "hot", "n"]
        if choice == 5:
            #rude customer
            print(f"{name}: Make me a medium sized hot black coffee, 1 sugar, no milk or ice. \nChop chop, make it quick\n")
            self.option = ["c", "m", "n", "1", "hot", "n"]

    def tea_options(self, name):
        #choice = randint(1, 5)

    def boba_options(self, name):
        #choice = randint(1, 5)
        

class RandomCustomer(Character):
    def perform_action(self, name):
        print(f"{name} is sitting enjoying their coffee. \"I don't need anything\"")
