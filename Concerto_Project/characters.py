from abc import ABC, abstractmethod
from random import randint
import random

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
            #cutie customer
            print(f"{name}: Hello, I'd like to get a large ice cold coffee, with no \nmilk and no sugar. Thank you!\n")
            self.option = ["c", "m", "n", "3", "c", "y"]
        elif choice == 4:
            print(f"{name}: Can I get a small coffee with not much sugar, no ice, and add milk. \nOh and make it really hot\n")
            self.option = ["c", "s", "y", "1", "h", "n"]
        elif choice == 5:
            #rude customer
            print(f"{name}: Make me a medium sized hot black coffee, 1 sugar, no milk or ice. \nChop chop, make it quick\n")
            self.option = ["c", "m", "n", "1", "h", "n"]

    def tea_option(self, name):
        choice = randint(1, 5)

        if choice == 1:
            #normal customer
            print(f"{name}: I would like a hot medium sized tea, lots of sugar and add milk please. \nForget the ice\n")
            self.option = ["t", "m", "y", "3", "h", "n"]
        elif choice == 2:
            print(f"{name}: Can I get a small iced tea with milk and extra ice? \nCan you put a little sugar in it as well?\n")
            self.option = ["t", "s", "y", "1", "c", "x"]
        elif choice == 3:
            #polite customer
            print(f"{name}: Hello, I'd like to get a large ice cold tea, with no milk and no sugar. thank you\n")
            self.option = ["t", "l", "n", "0", "c", "y"]
        elif choice == 4:
            print(f"{name}: Can I get a small tea with little sugar, no ice, and add milk. \nOh and make it really hot\n")
            self.option = ["t", "s", "y", "1", "h", "n"]
        elif choice == 5:
            #rude customer
            print(f"{name}: Make me a large hot tea as fast as you can, A LOT of sugar, no milk or ice. \nQuickly, don't waste my time.\n")
            self.option = ["t", "l", "n", "3", "h", "n"]
        
    def boba_option(self, name):
        choice = randint(1, 5)

        if choice == 1:
            #obnoxious customer
            print(f"{name}: Hi! Can I get a large boba with extra pearls! I love it when it's as cold as possible!\n Can you also add milk and a lot of sugar?!\n Thank you!!\n")
            self.option = ["b", "l", "y", "3", "c", "x", "y"]
        elif choice == 2:
            print(f"{name}: I want a small cold boba, no milk, please don't make it sweet, and can you add a little extra pearls? . \nOh and no ice please.\n")
            self.option = ["b", "s", "n", "0", "c", "n", "y"]
        elif choice == 3:
            print(f"{name}: Afternoon to you, I'd like a medium hot boba, with alot of milk and no ice. \nAlot of sugar please!!\n")
            self.option = ["b", "m", "y", "3", "h", "n", "n"]
        elif choice == 4:
            print(f"{name}: Can I get a large boba with not much sugar, a bit of ice, and add milk please.\n")
            self.option = ["b", "l", "y", "1", "c", "y", "n"]
        elif choice == 5:
            #rude customer
            print(f"{name}: I don't have all day so make me a small sized hot boba, very sweet with no milk or ice and extra pearls. \n Move it along now.\n")
            self.option = ["b", "s", "n", "3", "h", "n", "y"]
        
class NPC(ABC):
    def __init__(self, name):
        self._name = name
        self.new_dialogue = None
        self.dialogue = ["Thank you for the drink today", "The drink I had is amazing", "Can I sit here? \nYou: Of course you can",
                         "How are you barista? \nYou: I am alright, thank you for asking", "Can I order whenever I want to? \nYou: Yes you can"]

    @abstractmethod  # Declares an abstract method using a decorator.
    def perform_action(self):
        pass  # Abstract methods never contain any actual logic. The
        # transfer statement "pass" allows for this.

    # An abstract class must contain at least one abstract method.
    # However, "normal" methods may also be contained.

class ConcreteNPC(NPC):
    def perform_action(self):
        self.new_dialogue = random.choice(self.dialogue)
        print(f"{self._name} greets you politely.")
        print(f"{self._name}: \"{self.new_dialogue}\"")
