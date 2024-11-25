from loggable import Loggable
from characters import Character
import random
from time import sleep

class MakeDrink:
    def __init__(self):
        self.drink = None
        self.drink_name = None
        self.made_drink = []
        self.character = Character()
        self.size = None # s, m or l
        self.milk = None # yes or no
        self.sugar = None # 1, 2, or 3 spoons
        self.temp = None # hot, cold
        self.ice = None # yes, no, or extra
        self.boba = None # normal or extra
        self.log = Loggable()
        self.error_log = Loggable()

    def drink_options(self, name, day):
        # if not name:
        #     print("name not set")
        #     return

        drink_per_day = {
            1: "c", # coffee only
            2: "t", # tea only
            3: random.choice(["c", "t"]), # coffee and tea
            4: "b", # boba only
            5: random.choice(["c", "t", "b"]) # all three
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
        self.drink = input("What drink do you want to make. \n"
                           "'c' for coffee\n"
                           "'t' for tea\n"
                           "'b' for boba\n"
                           "Enter the drink you want to make: ")

        if self.drink not in ["c", "t", "b"]:
            print("This is not a drink option, try again!\n")
            self.drink_choice()
        else:
            self.made_drink.append(self.drink)

            if self.drink == "c":
                self.drink_name = "coffee"
            elif self.drink == "t":
                self.drink_name = "tea"
            elif self.drink == "b":
                self.drink_name = "boba"

        return self.drink

    def make_drink(self, name):
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



        self.made_drink.append(self.size)
        self.made_drink.append(self.milk)
        self.made_drink.append(self.sugar)
        self.made_drink.append(self.temp)
        self.made_drink.append(self.ice)
        if (self.drink == "b"):
            self.made_drink.append(self.boba)

        return self.made_drink
