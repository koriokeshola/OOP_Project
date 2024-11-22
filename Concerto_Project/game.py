from loggable import Loggable
from makeDrink import MakeDrink
from characters import Character
from achievements import Achievements #imports achievement class
import random
from time import sleep

class Game:
    """The Game class is set up to manage the game's behavior."""
    def __init__(self):
        # self.running is an instance variable within the Game class
        # This means that when an instance of the Game class is created,
        # the game loop will start running by default as it is set to True.
        self.__running = True
        self.start = False
        self.day = 1
        self.customers = 1
        self.make = MakeDrink()
        self.character = Character()
        self.name = None
        self.interact = False
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
        sleep_time = 0
        print("You're stumbling around in the cold, you can't feel your face... ")
        sleep(sleep_time)
        print("A strange figure approaches. You can't see in the harsh conditions.")
        sleep(sleep_time)
        print("He extends out his hand.. you reach out to take it.")
        sleep(sleep_time)
        print("He offers you a chance to redeem yourself, a nice job in a cosy cafe!")
        sleep(sleep_time)
        print("You accept... reluctantly.")
        sleep(sleep_time)
        print("Now your journey begins...")
        sleep(sleep_time)
        print("            G O L D E N   C A F É"
              "\n*******************************************"
              "\n|                                         |"
              "\n|     Serving Coffee, Tea, and Boba!      |"
              "\n|                                         |"
              "\n*******************************************\n")
        sleep(sleep_time * 2)
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
                    if self.interact is not True:
                        self.log.log("Player talks to the customer")
                        self.interact = True
                        self.drink_op()
                    else:
                        print(f"You already interacted with the {self.name}, please make their drink.\n")
                        self.update()
                elif player_input.lower() == "m":  # make a drink
                    if self.interact is True:
                        self.log.log("Player chooses to make a drink")
                        self.make_drink()
                    else:
                        print("You need to interact with the customer first.\n")
                        self.update()

    def drink_op(self):
        print(f"Customer {self.customers}")
        self.make.drink_options(self.name, self.day)
        self.update()

    def make_drink(self):
        self.make.drink_choice()

        self.make.make_drink(self.name)
        self.log.log("Player makes the drink")

    def start_game(self):
        """The start_game method introduces the player to the mystery case and
        sets the scene."""
        self.log.log("Game has begun.")
        print("\nGame intro")
        barista = input("What is your name: ")
        print(f"Hello {barista}, time to get working...\n")

        while self.day <= 5:
            print(f"\nDay {self.day}")
            ch_drk = self.day_drink[self.day]
            print(f"{ch_drk}\n")

            while self.customers <= 3:
                self.name = random.choice(self.character.name)
                self.update()

                if self.make.made_drink == self.make.character.option:
                    print(f"\nHurray, {self.name} is impressed")
                    self.log.log("Player impressed the customer")
                else:
                    print(f"\n{self.name} is disappointed")
                    self.log.log("Player disappoints the customer")

                self.customers = self.customers + 1
                self.make.drink = None
                self.make.made_drink = []  #bouthaynas line
                self.interact = False
                self.update()
            self.customers = 1
            self.day = self.day + 1

    def continue_game(self):
        #testing achievements
        self.achievement.unlock("You're a hard worker!")
        
        self.log.log("Player continued working")
