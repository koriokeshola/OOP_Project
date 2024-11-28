# Program Description: This program contains the functionality for
# taking user input to complete customer orders.

from loggable import Loggable
from characters import Character
import random
from time import sleep


class MakeDrink:
    """ A class that manages the process of making drinks based on customer orders.
    There are coffee, tea and boba options, and user input is taken to make the drinks
    according to the customer's order."""

    def __init__(self):
        self.drink = None  # drink options (c,t,b)
        self.drink_name = None  # full length of drink's name (coffe, tea, boba)
        self.made_drink = []  # stores drink details
        self.character = Character()  # customer interactions
        self.size = None  # s, m or l
        self.milk = None  # yes or no
        self.sugar = None  # 1, 2, or 3 spoons
        self.temp = None  # hot, cold
        self.ice = None  # yes, no, or extra
        self.boba = None  # normal or extra
        self.log = Loggable()  # instance for logging actions
        self.error_log = Loggable()  # instance logging errors

    def drink_options(self, name, day):
        """
        Determines the type of drink the customer can order basaed on the day.
        day 1 = coffee
        day 2 = tea
        day 3 = coffee or tea
        day 4 = boba
        day 5 = all three
        """
        drink_per_day = {
            1: "c",  # coffee only
            2: "t",  # tea only
            3: random.choice(["c", "t"]),  # coffee and tea
            4: "b",  # boba only
            5: random.choice(["c", "t", "b"])  # all three
        }

        # finds out the day number
        day_chosen = drink_per_day[day]

        if day_chosen == "c":
            self.character.coffee_option(name)
        elif day_chosen == "t":
            self.character.tea_option(name)
        elif day_chosen == "b":
            self.character.boba_option(name)

    # allows the user to choose the drink
    def drink_choice(self):
        # allows user to choose make the drinks
        self.drink = input("What drink do you want to make. \n"
                           "'c' for coffee\n"
                           "'t' for tea\n"
                           "'b' for boba\n"
                           "Enter the drink you want to make: ")
        # checks if you've entered valid inputs
        if self.drink not in ["c", "t", "b"]:
            print("This is not a drink option, try again!\n")
            self.drink_choice()
        else:
            # appends chosen drink type to the made_drink list
            self.made_drink.append(self.drink)

            if self.drink == "c":
                self.drink_name = "coffee"
            elif self.drink == "t":
                self.drink_name = "tea"
            elif self.drink == "b":
                self.drink_name = "boba"

        return self.drink

    def make_drink(self, name):
        # making the drink options
        self.size = input(f"Did {name} want small, medium, or large? [s, m, l]: ")  # s, m or l
        sleep(.5)
        while self.size not in ["s", "m", "l"]:
            print("Please pick s, m, or l\n")
            self.size = input(f"Did {name} want small, medium, or large? [s, m, l]: ")  # s, m or l

        self.milk = input(f"Did {name} want milk? yes or no?: [y, n]: ")  # yes or no
        sleep(.5)
        while self.milk not in ["y", "n"]:
            print("Please pick y or n\n")
            self.milk = input(f"Did {name} want milk? yes or no?: [y, n]: ")  # yes or no

        self.sugar = input(f"Did {name} want 0, 1 or 3 spoons of sugar? [0, 1, 3]: ")  # 0, 1, or 3 spoons
        sleep(.5)
        while self.sugar not in ["0", "1", "3"]:
            print("Please pick 0, 1, or 3\n")
            self.sugar = input(f"Did {name} want 0, 1 or 3 spoons of sugar? [0, 1, 3]: ")  # 0, 1, or 3 spoons

        self.temp = input(f"Did {name} want their {self.drink_name} hot or cold?: [h, c]: ")  # hot, cold
        sleep(.5)
        while self.temp not in ["h", "c"]:
            print("Please pick hot or cold\n")
            self.temp = input(f"Did {name} want their {self.drink_name} hot or cold?: [h, c]:  ")  # hot, cold

        self.ice = input(f"Did {name} want ice? yes, no, or extra?: [y, n, x]: ")  # yes, no, or extra
        sleep(.5)
        while self.ice not in ["y", "n", "x"]:
            print("Please pick y, n, or x\n")
            self.ice = input(f"Did {name} want ice? yes, no, or extra?: [y, n, x]: ")  # yes, no, or extra

        if self.drink == "b":
            while self.boba not in ["y", "n"]:
                print("Please pick y or n\n")
                self.boba = input(f"Did {name} want extra boba? yes or no?: [y, n]: ")  # yes or no

        # appends options to the made_drink list
        self.made_drink.append(self.size)
        self.made_drink.append(self.milk)
        self.made_drink.append(self.sugar)
        self.made_drink.append(self.temp)
        self.made_drink.append(self.ice)
        if self.drink == "b":
            self.made_drink.append(self.boba)

        return self.made_drink
