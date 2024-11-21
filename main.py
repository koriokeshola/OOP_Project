# CMPU 2016 Object-Oriented Programming
# TU857-2
# Semester 1 - Python with:
# Blessing Ugochukwu, C23342083
# Bouthayna Metarfi, C23306091
# Kori Okeshola, C23401212
# Seema Alazhari, C23405732
# Renee Low, C23321923
# Bartosz Sobiegraj, C23398751


# Program Description: This game is named "Golden Café".
# Users play as a barista to fulfill customer orders over a 5-day period.
# The aim is to complete the game at 100%, however you can progress even if
# you make some mistakes along the way.
# This project implements O.O.P principles such as abstraction, inheritance,
# polymorphism, encapsulation, file handling and modules.

from abc import ABC, abstractmethod
import random
from random import randint

class Loggable:
    def __init__(self):
        # Private variable to hold logs
        self._logs = []

    @property
    def logs(self):
        return self._logs  # Getter to access logs

    def log(self, message: str):
        # Method to log a message
        self._logs.append(message)

    def save_logs_to_file(self, filename):
        try:
            with open (filename, 'w') as log_file: # Open file in 'write' mode
                for log in self._logs:
                    log_file.write(log + '\n')  # Write each log on a
                    # new line
            print(f"Logs saved to {filename}")
        except Exception as e: # display error message in case of log entries
            # failing to save
            print(f"Log saving error occurred: {e}")

class Game:
    """The Game class is set up to manage the game's behavior."""

    def __init__(self):
        # self.running is an instance variable within the Game class
        # This means that when an instance of the Game class is created,
        # the game loop will start running by default as it is set to True.
        self.running = True
        self.start = False
        self.drink = None
        self.drink_name = None
        self.option = []
        self.made_drink = []
        self.size = None # s, m or l
        self.milk = None # yes or no
        self.sugar = None # 1, 2, or 3 spoons
        self.temp = None # hot, cold
        self.ice = None # yes, no, or extra
        self.name = ["Madoka", "Hugo", "Morgan", "Billy", "Renee", "Boots", "Mike Wazowski", "Big Guy", "Homura",
                     "Stinky Man", "Homeless Person", "Mike Tyson", "Toji", "Saitama"]
        self.day_drink = {
            1: "Serving Coffee Only Today", # coffee only
            2: "Serving Tea Only Today", # tea only
            3: "Serving Coffee and Tea Today", # coffee and tea
            4: "Serving Boba Only Today", # boba only
            5: "Serving Coffee, Tea, and Boba Today" # all three
        }

        self.log = Loggable()
        self.error_log = Loggable()
        self.log.log("Game initialised.")

    def run(self):
        """The run method starts the game loop and provides an introduction to
        the game."""
        self.log.log("Game is running.")

        print("You're stumbling around in the cold, you can't feel your face... "
              "\nA strange figure approaches. You can't see in the harsh conditions."
              "\nHe extends out his hand.. you reach out to take it."
              "\nHe offers you a chance to redeem yourself, a nice job in a cosy cafe!"
              "\nYou accept... reluctantly."
              "\nNow your journey begins...")
        print("\tG O L D E N   C A F É"
              "\n*******************************************"
              "\n|                                         |"
              "\n|     Serving Coffee, Tea, and Boba!      |"
              "\n|                                         |"
              "\n*******************************************\n")
        print("Now that you have started your job, you will have to satisfy customers everyday!")

        while self.running:
            self.update()

    def rules(self):
        print("\n*******************************************"
              "\n|          H O W  T O  P L A Y            |"
              "\n|                                         |"
              "\n|  1. There are 3 Customers Per Day       |"
              "\n|  2. Each Day has New Menu Options       |"
              "\n|  3. Pay Attention to Customer Orders    |"
              "\n|  4. Choose the Right Ingredients        |"
              "\n|  5. Earn Stars to Level Up              |"
              "\n|  6. Unlock Achievements                 |"
              "\n|  7. Handle Special Requests             |"
              "\n|                                         |"
              "\n|       !! TRY NOT TO GET FIRED !!        |"
              "\n*******************************************\n")

    def update(self):
        """The update method waits for player input and responds to their
        choice to start the game or quit."""
        if not self.start:
            player_input = input("Press 'q' to quit, 'r' for rules or 's' to start: ")
            if player_input.lower() == "q":
                # we exit the game running loop by setting this flag variable
                # to False
                self.__running = False
                filename = input(
                    "Please enter a file name of the template <filename.txt> in order to save the game logs: ")
                self.log.save_logs_to_file(filename)
                self.log.log("Player quits the game")
                self.running = False
            elif player_input.lower() == "s":
                self.game_started = True
                self.start = True
                self.start_game()
                self.log.log("Player starts the game")
            elif player_input.lower() == "r":
                self.rules()
                self.log.log("Player checks the rules")
        else:  # if user chooses to continue they get more options
            player_input = input("Press 'q' to quit, 'i' to interact, 'm' to make drink, or 'c' to continue: ")
            if player_input.lower() == "q":  # quits game
                self.__running = False
                filename = input(
                    "Please enter a file name of the template <filename.txt> in order to save the game logs: ")
                self.log.save_logs_to_file(filename)
                self.log.log("Player quits the game")
                self.running = False
            elif player_input.lower() == "c":  # continues game
                self.log.log("Player continued working")
                self.continue_game()
            elif player_input.lower() == "i":  # interacts with customer
                self.log.log("Player talks to the customer")
                self.continue_game()
            elif player_input.lower() == "m":  # chooses a door
                self.log.log("Player chooses to make a drink")
                self.make_drink()

    def coffee_option(self, name):
        #choice = randint(1, 5)

        #if choice == 1:
            print(f"{name}: I would like a medium sized, hot coffee without milk and 3 sugars.\nPlease no ice\n")
            self.option = ["c", "m", "n", "3", "hot", "n"]


    def drink_options(self, name, day):
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
            self.coffee_option(name)
        # elif day_chosen == "t":
        #     self.tea_option(name)
        # elif day_chosen == "b":
        #     self.boba_option(name)




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
        while self.size not in ["s", "m", "l"]:
            print("Please pick s, m, or l\n")
            self.size = input(f"Did {name} want small, medium, or large? [s, m, l]: ")  # s, m or l

        self.milk = input(f"Did {name} want milk? yes or no?: [y, n]: ")  # yes or no
        while self.milk not in ["y", "n"]:
            print("Please pick y or n\n")
            self.milk = input(f"Did {name} want milk? yes or no?: [y, n]: ")  # yes or no

        self.sugar = input(f"Did {name} want 0, 1 or 3 spoons of sugar? [0, 1, 3]: ")  # 0, 1, or 3 spoons
        while self.sugar not in ["0", "1", "3"]:
            print("Please pick 0, 1, or 3\n")
            self.sugar = input(f"Did {name} want 0, 1 or 3 spoons of sugar? [0, 1, 3]: ")  # 0, 1, or 3 spoons

        self.temp = input(f"Did {name} want their {self.drink_name} hot or cold?: ")  # hot, cold
        while self.temp not in ["hot", "cold"]:
            print("Please pick hot or cold\n")
            self.temp = input(f"Did {name} want their {self.drink_name} hot or cold?: ")  # hot, cold

        self.ice = input(f"Did {name} want ice? yes, no, or extra?: [y, n, x]: ")  # yes, no, or extra
        while self.ice not in ["y", "n", "x"]:
            print("Please pick y, n, or x\n")
            self.ice = input(f"Did {name} want ice? yes, no, or extra?: [y, n, x]: ")  # yes, no, or extra

        self.made_drink.append(self.size)
        self.made_drink.append(self.milk)
        self.made_drink.append(self.sugar)
        self.made_drink.append(self.temp)
        self.made_drink.append(self.ice)

        return self.made_drink


    def start_game(self):
        """The start_game method introduces the player to the mystery case and
        sets the scene."""
        self.log.log("Game has begun.")
        print("\nGame intro")
        day = 1
        customers = 1

        while day <= 5:
            print(f"\nDay {day}")
            ch_drk = self.day_drink[day]
            print(f"{ch_drk}\n")
            self.update()

            while customers <= 3:
                name = random.choice(self.name)

                print(f"Customer {customers}")
                self.drink_options(name, day)

                self.drink_choice()

                self.make_drink(name)

                if self.made_drink == self.option:
                    print(f"\nHurray, {name} is impressed")
                else:
                    print(f"\n{name} is disappointed")
                    customers = customers + 1
                    self.drink = None
                self.made_drink = []  #bouthaynas line
                self.update()
            customers = 1
            day = day + 1





    def continue_game(self):
        print("You continue working...\n")
        self.log.log("Player continued working")


# runs the game from the Game function
if __name__ == "__main__":
    game = Game()
    game.run()

    print("\nGame Logs:")
    for log in game.log.logs:
        print(log)

    print("\nGame Error Logs:")
    for log in game.error_log.logs:
        print(log)
