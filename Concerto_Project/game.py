from loggable import Loggable
from makeDrink import MakeDrink
from characters import Character
import random

class Game:
    """The Game class is set up to manage the game's behavior."""

    def __init__(self):
        # self.running is an instance variable within the Game class
        # This means that when an instance of the Game class is created,
        # the game loop will start running by default as it is set to True.
        self.__running = True
        self.start = False
        self.make = MakeDrink()
        self.character = Character()
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

        while self.__running:
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
        player_input = None
        if not self.start:
            while player_input not in ["q", "r", "s"]:
                player_input = input("Press 'q' to quit, 'r' for rules or 's' to start: ")
                if player_input.lower() == "q":
                    # we exit the game running loop by setting this flag variable
                    # to False
                    self.__running = False
                    filename = input(
                        "Please enter a file name of the template <filename.txt> in order to save the game logs: ")
                    self.log.save_logs_to_file(filename)
                    self.log.log("Player quits the game")
                    self.__running = False
                elif player_input.lower() == "s":
                    self.start = True
                    self.start_game()
                    self.log.log("Player starts the game")
                elif player_input.lower() == "r":
                    self.rules()
                    self.log.log("Player checks the rules")
        else:  # if user chooses to continue they get more options
            while player_input not in ["q", "i", "m", "c"]:
                player_input = input("Press 'q' to quit, 'i' to interact, 'm' to make drink, or 'c' to continue: ")
                if player_input.lower() == "q":  # quits game
                    self.__running = False
                    filename = input(
                        "Please enter a file name of the template <filename.txt> in order to save the game logs: ")
                    self.log.save_logs_to_file(filename)
                    self.log.log("Player quits the game")
                    self.__running = False
                elif player_input.lower() == "c":  # continues game
                    self.log.log("Player continued working")
                    self.continue_game()
                elif player_input.lower() == "i":  # interacts with customer
                    self.log.log("Player talks to the customer")
                    self.continue_game()
                elif player_input.lower() == "m":  # chooses a door
                    self.log.log("Player chooses to make a drink")
                    self.make.make_drink()

    def start_game(self):
        """The start_game method introduces the player to the mystery case and
        sets the scene."""
        self.log.log("Game has begun.")
        print("\nGame intro")
        barista = input("What is your name: ")
        print(f"Hello {barista}, time to get working...\n")

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
                self.make.drink_options(name, day)

                self.make.drink_choice()

                self.make.make_drink(name)
                self.log.log("Player makes the drink")

                if self.make.made_drink == self.make.character.option:
                    print(f"\nHurray, {name} is impressed")
                    self.log.log("Player impressed the customer")
                else:
                    print(f"\n{name} is disappointed")
                    self.log.log("Player disappoints the customer")
                    customers = customers + 1
                    self.make.drink = None
                self.make.made_drink = []  #bouthaynas line
                self.update()
            customers = 1
            day = day + 1

    def continue_game(self):
        print("You continue working...\n")
        self.log.log("Player continued working")
