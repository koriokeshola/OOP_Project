# Program Description: Program which controls NPC and Customer interactions,
# allows the customers to be randomised as well as their drinks.
# Includes abstract methods within the NPC class.

# Importing necessary libraries.
from abc import ABC, abstractmethod
from random import randint
import random


class Character(ABC):  # Make Character an abstract class.
    """The Character class has been transformed into an
    abstract class by using the ABC class.
    An abstract method named perform_action has been declared in the
    Character class. It then implements this
    abstract method with specific actions that demonstrate polymorphism."""

    def __init__(self):
        # Creating names and options list for verifying customer orders.
        self.option = []
        self.name = ["Madoka", "Hugo", "Morgan", "Billy", "Renee", "Boots", "Mike Wazowski", "Big Guy", "Homura",
                     "Stinky Man", "Homeless Person", "Mike Tyson", "Toji", "Saitama", "Humbleness Personified"]

    # @abstractmethod
    def perform_action(self, name):
        pass

    def coffee_option(self, name):
        choice = randint(1, 5)  # Choosing a variation of what the customer would like to order.

        if choice == 1:
            # Regular customer.
            print(f"{name}: I would like a medium sized, hot coffee without milk and 3 sugars.\nPlease no ice")
            self.option = ["c", "m", "n", "3", "h", "n"]  # Input that the player has to put in for them to gain a star.
        elif choice == 2:
            # Regular customer.
            print(f"{name}: I want a large hot coffee, add some milk, dont make it sweet. \nForget the ice")
            self.option = ["c", "l", "y", "0", "h", "n"]  # Input that the player has to put in for them to gain a star.
        elif choice == 3:
            # Cutie customer.
            print(f"{name}: Hello, I'd like to get a large ice cold coffee, with no \nmilk and no sugar. Thank you!")
            self.option = ["c", "l", "n", "0", "c", "y"]  # Input that the player has to put in for them to gain a star.
        elif choice == 4:
            # Regular customer.
            print(
                f"{name}: Can I get a small coffee with not much sugar, no ice, and add milk. \nOh and make it really hot")
            self.option = ["c", "s", "y", "1", "h", "n"]  # Input that the player has to put in for them to gain a star.
        elif choice == 5:
            # Rude customer
            print(
                f"{name}: Make me a medium sized hot black coffee, 1 sugar, no milk or ice. \nChop chop, make it quick")
            self.option = ["c", "m", "n", "1", "h", "n"]  # Input that the player has to put in for them to gain a star.

    def tea_option(self, name):
        choice = randint(1, 5)  # choosing a variation of what the customer would like to order

        if choice == 1:
            # Regular customer.
            print(f"{name}: I would like a hot medium sized tea, lots of sugar and add milk please. \nForget the ice")
            self.option = ["t", "m", "y", "3", "h", "n"]  # Input that the player has to put in for them to gain a star.
        elif choice == 2:
            # Polite customer.
            print(
                f"{name}: Can I get a small iced tea with milk and extra ice? \nCan you put a little sugar in it as well?")
            self.option = ["t", "s", "y", "1", "c", "x"]  # Input that the player has to put in for them to gain a star.
        elif choice == 3:
            # Polite customer.
            print(f"{name}: Hello, I'd like to get a large ice cold tea, with no milk and no sugar. thank you")
            self.option = ["t", "l", "n", "0", "c", "y"]  # Input that the player has to put in for them to gain a star.
        elif choice == 4:
            # Regular customer.
            print(
                f"{name}: Can I get a small tea with little sugar, no ice, and add milk. \nOh and can you make it really hot")
            self.option = ["t", "s", "y", "1", "h", "n"]  # Input that the player has to put in for them to gain a star.
        elif choice == 5:
            # Rude customer.
            print(
                f"{name}: Make me a large hot tea as fast as you can, A LOT of sugar, no milk or ice. \nQuickly, don't waste my time.")
            self.option = ["t", "l", "n", "3", "h", "n"]  # Input that the player has to put in for them to gain a star.

    def boba_option(self, name):
        choice = randint(1, 5)  # choosing a variation of what the customer would like to order

        if choice == 1:
            # Obnoxious customer.
            print(
                f"{name}: Hi! Can I get a large boba with extra pearls! I love it when it's as cold as possible!\n Can you also add milk and a lot of sugar?! Thank you!!")
            self.option = ["b", "l", "y", "3", "c", "x",
                           "y"]  # Input that the player has to put in for them to gain a star.
        elif choice == 2:
            # Regular customer.
            print(
                f"{name}: I want a small cold boba, no milk, please don't make it sweet, and can you add a little extra pearls? . \nOh and no ice please.")
            self.option = ["b", "s", "n", "0", "c", "n",
                           "y"]  # Input that the player has to put in for them to gain a star.
        elif choice == 3:
            # Polite Customer.
            print(
                f"{name}: Afternoon to you, I'd like a medium hot boba, with alot of milk and no ice. \nAlot of sugar please!!")
            self.option = ["b", "m", "y", "3", "h", "n",
                           "n"]  # Input that the player has to put in for them to gain a star.
        elif choice == 4:
            # Polite customer.
            print(f"{name}: Can I get a large boba with not much sugar, a bit of ice, and add milk please.")
            self.option = ["b", "l", "y", "1", "c", "y",
                           "n"]  # Input that the player has to put in for them to gain a star.
        elif choice == 5:
            # Rude customer.
            print(
                f"{name}: I don't have all day so make me a small sized hot boba, very sweet with no milk or ice and extra pearls. \n Move it along now.")
            self.option = ["b", "s", "n", "3", "h", "n",
                           "y"]  # Input that the player has to put in for them to gain a star.


class NPC(ABC):  # Abstracted class.
    def __init__(self, name):
        self._name = name  # internal use variable
        self.new_dialogue = None
        self.dialogue = ["Thank you for the drink today", "The drink I had is amazing",
                         "Can I sit here? \nYou: Of course you can",
                         "How are you barista? \nYou: I am alright, thank you for asking",
                         "Can I order whenever I want to? \nYou: Yes you can"]

    @abstractmethod  # Declares an abstract method using a decorator.
    def perform_action(self):
        pass  # Abstract methods never contain any actual logic. The
        # transfer statement "pass" allows for this.

    # An abstract class must contain at least one abstract method.
    # However, "normal" methods may also be contained.


class ConcreteNPC(NPC):  # Inheritance from NPC.
    def perform_action(self):
        self.new_dialogue = random.choice(self.dialogue)  # Chooses randomly from the choice list.
        print(
            f"{self._name} greets you politely.")  # Uses the same name for each customer so that it can't be confused.
        print(f"{self._name}: \"{self.new_dialogue}\"")
