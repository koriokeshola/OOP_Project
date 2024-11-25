from abc import ABC, abstractmethod
from random import randint


class Character(ABC):  # Make Character an abstract class
    """In this solution, the Character class has been transformed into an
    abstract class by using the ABC class.
    An abstract method named perform_action has been declared in the
    Character class. The  then implement this
    abstract method with specific actions that demonstrate polymorphism. """

    def __init__(self):
        # Even in abstract classes we see encapsulation  as before.
        self.option = []
        self.name = ["Madoka", "Hugo", "Morgan", "Billy", "Renee", "Boots", "Mike Wazowski", "Big Guy", "Homura",
                     "Stinky Man", "Homeless Person", "Mike Tyson", "Toji", "Saitama", "Humbleness Personified"]

    # @abstractmethod
    def perform_action(self, name):
        pass

    def coffee_option(self, name):
        choice = randint(1, 5)

        if choice == 1:
            print(f"{name}: I would like a medium sized, hot coffee without milk and 3 sugars.\nPlease no ice\n")
            self.option = ["c", "m", "n", "3", "h", "n"]
        elif choice == 2:
            print(f"{name}: I want a large hot coffee, add some milk, dont make it sweet. \nForget the ice\n")
            self.option = ["c", "l", "y", "0", "h", "n"]
        elif choice == 3:
            # cutie customer
            print(f"{name}: MORNING, I'd like a medium ice cold coffee, with alot of milk. \nAlot of sugar please!!\n")
            self.option = ["c", "m", "y", "3", "c", "y"]
        elif choice == 4:
            print(
                f"{name}: Can I get a small coffee with not much sugar, no ice, and add milk. \nOh and make it really hot\n")
            self.option = ["c", "s", "y", "1", "h", "n"]
        elif choice == 5:
            # rude customer
            print(
                f"{name}: Make me a medium sized hot black coffee, 1 sugar, no milk or ice. \nChop chop, make it quick\n")
            self.option = ["c", "m", "n", "1", "h", "n"]

    def tea_option(self, name):
        choice = randint(1, 5)

        if choice == 1:
            print(f"{name}: I would like a hot medium sized tea, lots of sugar and add milk please. \nForget the ice\n")
            self.option = ["t", "m", "y", "3", "h", "n"]
        elif choice == 2:
            print(
                f"{name}: Can I get a small iced tea with milk and extra ice? \nCan you put a little sugar in it as well?\n")
            self.option = ["t", "s", "y", "1", "c", "x"]
        elif choice == 3:
            # cutie customer
            print(f"{name}: Hello, I'd like to get a large ice cold tea, with no milk and no sugar. Thank you!\n")
            self.option = ["c", "m", "y", "3", "c", "y"]
        elif choice == 4:
            print(
                f"{name}: Can I get a small tea with little sugar, no ice, and add milk. \nOh and make it really hot\n")
            self.option = ["c", "s", "y", "1", "h", "n"]
        elif choice == 5:
            # rude customer
            print(
                f"{name}: Make me a large hot tea as fast as you can, A LOT of sugar, no milk or ice. \nQuickly, don't waste my time.\n")
            self.option = ["c", "m", "n", "1", "h", "n"]

    def boba_option(self, name):
        choice = randint(1, 5)

        if choice == 1:
            print(f"{name}: I would like a large, cold boba with milk and 1 sugar.\nExtra ice please!\n")
            self.option = ["b", "l", "y", "1", "cold", "x"]
        if choice == 2:
            print(
                f"{name}: I want a warm boba in the biggest cup you have, lots of milk and no sugar. \nNo ice please!\n")
            self.option = ["b", "l", "y", "0", "hot", "n"]
        if choice == 3:
            # cutie customer
            print(
                f"{name}: MORNING! I'd like a medium cold boba, with some milk. \nOne sugar, no ice and please take your time!!\n")
            self.option = ["b", "m", "y", "1", "cold", "n"]
        if choice == 4:
            print(
                f"{name}: Can I get a small cold boba, with milk and a LOT of sugar. \nI'd like some ice too.\n")
            self.option = ["b", "s", "y", "3", "cold", "y"]
        if choice == 5:
            # rude customer
            print(
                f"{name}: I want a big cup of boba, tiny bit of sugar, no milk and some ice. \nI haven't got all day ya know!\n")
            self.option = ["b", "l", "n", "1", "cold", "y"]


class RandomCustomer(Character):
    def perform_action(self, name):
        print(f"{name} is sitting enjoying their coffee. \"I don't need anything\"")
