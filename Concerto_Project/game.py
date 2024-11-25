from loggable import Loggable
from makeDrink import MakeDrink
from characters import Character
from characters import ConcreteNPC
from achievements import Achievements  # imports achievement class
from design import printing_day
from design import type_text
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
        self.sleep_time = 0
        self.make = MakeDrink()
        self.character = Character()
        self.name = None
        self.interact = False
        self.day_drink = {
            1: "Serving Coffee Only Today",  # coffee only
            2: "Serving Tea Only Today",  # tea only
            3: "Serving Coffee and Tea Today",  # coffee and tea
            4: "Serving Boba Only Today",  # boba only
            5: "Serving Coffee, Tea, and Boba Today"  # all three
        }
        self.log = Loggable()
        self.error_log = Loggable()
        self.achievement = Achievements()
        self.log.log("Game initialised.")

    def run(self):
        """The run method starts the game loop and provides an introduction to
        the game."""
        self.log.log("Game is running.")

        type_text("You're stumbling around in the cold, you can't feel your face... ")
        sleep(self.sleep_time)
        type_text("A strange figure approaches. You can't see in the harsh conditions.")
        sleep(self.sleep_time)
        type_text("He extends out his hand.. you reach out to take it.")
        sleep(self.sleep_time)
        type_text("He offers you a chance to redeem yourself, a nice job in a cosy cafe!")
        sleep(self.sleep_time)
        type_text("You accept... reluctantly.")
        sleep(self.sleep_time)
        type_text("Now your journey begins...")
        sleep(self.sleep_time)
        
        print("\033[1;33m            G O L D E N   C A F É\033[0m"  # Bold, Yellow Text
              "\n\033[1;36m*******************************************\033[0m"  # Cyan
              "\n\033[1;36m|                                         |\033[0m"
              "\n\033[1;36m|\033[0m     Serving Coffee, Tea, and Boba!      \033[1;36m|\033[0m"
              "\n\033[1;36m|                                         |\033[0m"
              "\n\033[1;36m*******************************************\033[0m")  # Cyan
        """
        #using ANSI Escape Sequences for coloring text in
        print("\033[1;33m            G O L D E N   C A F É\033[0m"  # Bold, Yellow Text
              "\n\033[1;36m*******************************************\033[0m"  # Cyan
              "\n\033[1;36m|                                         |\033[0m")
        type_text("\t serving Coffee, Tea, and Boba!")
        print("\n\033[1;36m|                                         |\033[0m"
              "\n\033[1;36m*******************************************\033[0m\n")  # Cyan
        """
        sleep(self.sleep_time * 2)
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
            while player_input not in ["q", "i", "m", "c", "r"]:
                player_input = input("Press 'q' to quit, 'i' to interact, 'm' to make drink, 'c' to continue, or\n'r' for NPC interaction: ")
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
                elif player_input.lower() == "m":  # chooses a door
                    if self.interact is True:
                        self.log.log("Player chooses to make a drink")
                        self.make_drink()
                    else:
                        print("You need to interact with the customer first.\n")
                        self.update()
                elif player_input.lower() == "r":
                    self.interact_with_customers()

    def interact_with_customers(self):
        self.name = random.choice(self.character.name)
        print("")
        npc = ConcreteNPC(self.name)
        npc.perform_action()
        print("")
        self.update()
    
    def drink_op(self):
        print(f"\nCustomer {self.customers}")
        self.make.drink_options(self.name, self.day)
        self.update()

    def make_drink(self):
        self.make.drink_choice()

        self.make.make_drink(self.name)
        self.log.log("Player makes the drink")
        self.interact = False

    def start_game(self):
        """The start_game method introduces the player to the mystery case and
        sets the scene."""
        self.log.log("Game has begun.")
        print("\nGame intro")
        barista = input("What is your name: ")
        print(f"Hello {barista}, time to get working...\n")
        total_stars = 0

        while self.day <= 5 and self.__running:
            if self.__running is True:
                printing_day(self.day)  #prints what day it is  Seemas code
                ch_drk = self.day_drink[self.day]
                print(f"\n{ch_drk}\n")
                stars = 0
            else:
                quit(self.start_game())

            while self.customers <= 3 and self.__running:
                self.name = random.choice(self.character.name)
                if self.__running is True:
                    #print("hello")
                    self.update()

                    if self.make.made_drink and self.interact == False:
                        if self.make.made_drink == self.make.character.option:
                            print(f"\nHurray, {self.name} is impressed")
                            self.log.log(f"Player impressed {self.name} with perfect drink")
                            stars += 1
                        else:
                            print(f"\n{self.name} is disappointed")

                            self.achievement.unlock("You've disappointed your first customer...")
                            self.log.log(f"Achievement unlocked: Player disappoints {self.name}")
                        self.customers = self.customers + 1
                        self.make.drink = None
                        self.make.made_drink = []  # bouthaynas line
                    else :
                        self.log.log("Didn't Finish Job")
                else:
                    quit(self.start_game())
            self.customers = 1
            sleep(self.sleep_time * 2)
            if self.day == 1:
                self.achievement.unlock("You survived your first day on the job!")
                self.log.log("Achievement unlocked: Player finished Day 1")
            elif self.day == 2:
                self.achievement.unlock("You completed day 2!")
                self.log.log("Achievement unlocked: Player finished Day 2")
            elif self.day == 3:
                self.achievement.unlock("You completed day 3!")
                self.log.log("Achievement unlocked: Player finished Day 3")
            elif self.day == 4:
                self.achievement.unlock("You completed day 4!")
                self.log.log("Achievement unlocked: Player finished Day 4")
            else:
                self.achievement.unlock("You completed day 5!")
                self.log.log("Achievement unlocked: Player finished Day 5")
            self.day = self.day + 1

            total_stars += stars  # sum of stars
            if stars == 1:
                print(f"You earned {stars} star today!")
            else:
                print(f"You earned {stars} stars today!")
            sleep(self.sleep_time * 2)
            if self.day == 5:
                print(f"You earned a total of {total_stars} this week!")
                sleep(self.sleep_time * 2)
                if total_stars == 15:
                    self.achievement.unlock("Maximum stars achieved!")
                    self.log.log("Achievement unlocked: Best Barista to exist")
                if total_stars == 0:
                    self.achievement.unlock("Wow, you did not earn a single star...")
                    self.log.log("Achievement unlocked: How do you manage...")
            sleep(self.sleep_time * 2)

    def continue_game(self):
        print("You continue working...\n")

        # testing achievements
        self.achievement.unlock("You're a hard worker!")
        self.achievements += 1
        self.log.log("Player continued working")
        self.update()
