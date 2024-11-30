# Program description: Main program branch operator, allows for all the modules within the folder
# to work here, allows for player to start, continue, and exit the game. Gives the player
# interaction choices with the customer through various classes and methods.
# Logs each action done by the player through a module, allows player to make and perform actions
# Main body of the Game.

# Import relevant classes and methods
from loggable import Loggable
from makeDrink import MakeDrink
from characters import Character
from characters import ConcreteNPC
from characters import NormalNPC
from achievements import Achievements
from reviews import Reviews
from design import printing_day
from design import type_text
import random  # For randomisation of character names
from time import sleep  # For display purposes

class Game:
    """The Game class is set up to manage the game's behavior."""
    def __init__(self):
        """ Variables used to manage game logic, including:
        The game's running state, initialised values and instructions for tracking
        current character/day,
        Boolean values to track game progression and current running state,
        Helper class instances for drink making character interactions, logging,
        achievements and reviews.
        For example, self.running is an instance variable within the Game class
        This means that when an instance of the Game class is created,
        the game loop will start running by default as it is set to True. """

        self.__running = True # Whether the game is running
        self.start = False # Whether the game has started
        self.interact = False # Whether player has interacted with a customer
        self.day = 1 # What current day it is in-game
        self.long = 0 # Amount of time the customer interacted with waits
        self.customers = 1 # What customer it is
        self.sleep_time = 1 # How long the delay is
        self.achievements = 0 # How many achievements the user has received
        self.review_count = 0 # # How many reviews the player has gotten thus far
        self.make = MakeDrink() # Variable for a Module
        self.character = Character() # Variable for a Module
        self.review = Reviews() # Variable for a Module
        self.log = Loggable() # Variable for a Module
        self.error_log = Loggable() # Variable for a Module
        self.achievement = Achievements() # Variable for a Module
        self.name = None # Name that'll be used from character Module
        self.player_input = None # Player input for when they choose actions
        self.day_drink = { # Instructions
            1: "Serving Coffee Only Today",
            2: "Serving Tea Only Today",
            3: "Serving Coffee and Tea Today",
            4: "Serving Boba Only Today",
            5: "Serving Coffee, Tea, and Boba Today"
        }
        self.log.log("Game initialised.")

    def run(self):
        """The run method starts the game loop and provides an introduction to the game."""
        self.log.log("Game is running.")

        # Animated game intro
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

        sleep(self.sleep_time * 2)  # slight delay between displaying next line
        print("Now that you have started your job, you will have to satisfy customers everyday!")

        while self.__running: # Calling another method within the class to update the game
            self.update()

    def rules(self):
        """ Method which displays rules when requested. """
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
        choice to start game, quit, display rules, interact with a customer,
        make drink, continue, interact with an NPC or read reviews."""
        if self.long > 2 and self.interact == True: # times the players actions
            print(f"\033[1;31m{self.name}: Hey where is my drink at?\033[0m")
        try:
            self.player_input = None
            if not self.start:
                while self.player_input not in ["q", "r", "s"]:
                    self.player_input = input("Press 'q' to quit, 'r' for rules or 's' to start: ")
                    if self.player_input.lower() not in ["q", "r", "s"]:
                        raise ValueError("Please choose a valid letter")
                    if self.player_input.lower() == "q":
                        self.log.log("Player quits the game")
                        # Save game logs to a file to display complete gameplay sequence
                        filename = input("Please enter a file name of the template <filename.txt> in order to save the game logs: ")
                        self.log.save_logs_to_file(filename)
                        # we exit the game running loop by setting this flag variable to False
                        self.__running = False
                    elif self.player_input.lower() == "s":
                        # Allows the game to start
                        self.start = True
                        self.log.log("Player starts the game")
                        self.start_game()
                    elif self.player_input.lower() == "r":
                        # Lets the player read the rules
                        self.rules()
                        self.log.log("Player checks the rules")
        # Exception handling in case of incorrect character input or sudden error
        except ValueError as ve:
            print(f"Error: {ve}. Please try again")
            self.log.log(f"Incorrect Input: {ve}")
            # self.update()
        except Exception as e:
            print(f"Error: {e}. An unexpected error occurred.")
            self.log.log(f"Unexpected Error: {e}")
            filename = input("Please enter a file name of the template <filename.txt> in order to save the game logs: ")
            self.log.save_logs_to_file(filename)
            self.__running = False  # stop game upon critical error
        else:  # if user chooses to continue they get more options
            while self.player_input not in ["q", "i", "m", "c", "n", "r"]:
                self.player_input = input(
                    "Press 'q' to quit, 'i' to interact, 'm' to make drink, 'c' to continue, \n'r' to see reviews or 'n' for NPC interaction: ")
                if self.player_input.lower() == "q":  # quits game
                    self.log.log("Player quits the game")
                    # Save game logs to a file to display complete gameplay sequence
                    filename = input("Please enter a file name of the template <filename.txt> in order to save the game logs: ")
                    self.log.save_logs_to_file(filename)
                    # we exit the game running loop by setting this flag variable to False
                    self.__running = False
                elif self.player_input.lower() == "c":  # continues game
                    self.log.log("Player continued working.")
                    self.continue_game()
                elif self.player_input.lower() == "r":  # Print reviews, if any
                    if self.review_count <= 0:
                        print("You have not gotten any reviews yet.\n")
                        self.log.log("Player checks the Reviews.")
                    else:
                        self.log.log("Player checks the Reviews.")
                        print("\033[1;32;40mReviews:\033[0m")
                        for item in self.review.reviews:
                            print(item, " ")
                        print("")
                elif self.player_input.lower() == "i":  # interacts with customer
                    if not self.interact:
                        self.log.log("Player talks to a customer")
                        self.interact = True
                        self.drink_op()
                    else:
                        print(f"You already interacted with {self.name}, please make their drink.\n")
                        self.update()
                elif self.player_input.lower() == "m":  # Make a drink, only after interaction
                    if self.interact:
                        self.log.log("Player chooses to make a drink")
                        self.make_drink()
                    else:
                        print("You need to interact with the customer first.\n")
                        self.update()
                elif self.player_input.lower() == "n":  # Interact with an NPC
                    self.interact_with_customers()
                    self.log.log("Player chats with a nearby NPC.")


    def interact_with_customers(self):
        """Interact with an NPC by creating a randomised instance of the
        abstract ConcreteNPC class."""

        npc_name = random.choice(self.character.name)
        new_npc_name = random.choice(self.character.name)
        print("")
        npc = ConcreteNPC(npc_name)
        normal_npc = NormalNPC(new_npc_name)
        npc.perform_action()
        normal_npc.perform_action()
        print("")
        if self.interact:
            self.long += 1
        self.update()


    def drink_op(self):
        """This method provides the list of currently available drink options."""
        print(f"\n\033[1;34mCustomer {self.customers}")
        self.make.drink_options(self.name, self.day)
        print("\033[0m")
        self.update()


    def make_drink(self):
        """This method allows user to set the chosen drink, proceed to make it,
        and resets interaction instance to allow user to proceed to the next customer. """
        self.make.drink_choice()

        self.make.make_drink(self.name)
        self.log.log("Player makes the drink")
        self.interact = False
        self.long = 0 # sets amount of time the customer waited to 0


    def start_game(self):
        """The start_game method introduces the player to the café game and sets the scene.
        Additionally, it contains logic for displaying what day it is, ensuring only 3
        customers are served per day, determining customer satisfaction by confirming
        whether the user-selected ingredients for each order are correct and tracking reviews."""
        self.log.log("Game has begun.")
        # print("\nGame intro")
        barista = input("What is your name: ")
        print(f"Hello {barista}, time to get working...\n")
        self.log.log("Player Gets Hired!")
        total_stars = 0

        while self.day <= 5 and self.__running:  # while the game is not completed
            if self.__running:
                printing_day(self.day)  # determine current day and available drink options
                ch_drk = self.day_drink[self.day]
                print(f"\n{ch_drk}\n")
                stars = 0  # initialise stars to zero at the start of each day
            else:
                return

            while self.customers <= 3 and self.__running: # Check to see if all customers have been served for the day
                self.name = random.choice(self.character.name)
                if self.__running:
                    if self.player_input != "q":  # proceed if user has not decided to quit
                        self.update()

                        if self.make.made_drink and self.interact == False: # Dramatic effect code to see if the player got the order correct
                            print(f"\n{self.name} collects their drink and takes a sip...")
                            sleep(self.sleep_time)
                            if self.make.made_drink == self.make.character.option: # Player successfully makes the drink correctly
                                print(f"{self.name}: Thank you! This is delicious!")
                                self.log.log(f"Player impressed {self.name} with perfect drink")
                                stars += 1 # Adds a star to the total star counter
                                self.review_count = + 1
                                self.review.add_good_reviews(self.name)
                            else:  # if order is made incorrectly
                                print(f"{self.name}: EUGH!! This is NOT what I ordered!" # Player fails to make the drink correctly
                                      f"\n{self.name} is disappointed")
                                self.review_count = + 1
                                self.review.add_bad_reviews(self.name) # adds a bad review to the review list
                                self.achievement.unlock("You've disappointed your first customer...")
                                self.log.log(f"Achievement unlocked: Player disappoints {self.name}")
                            self.log.log("Customer leaves a new review.")
                            self.customers += 1
                            self.make.drink = None  # reset make drink
                            self.make.made_drink = []
                        else:
                            self.log.log("Didn't Finish Job")
                    else:  # return if user decides to quit
                        return
            self.customers = 1  # reset customer count for following day
            sleep(self.sleep_time * 2)  # slight delay before printing achievement
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

            total_stars += stars  # sum of stars
            if stars == 1:  # print "star" or "stars" based on amount earned
                print(f"You earned {stars} star today!")
            else:
                print(f"You earned {stars} stars today!")
            sleep(self.sleep_time * 2)
            if self.day == 5:
                print(f"You earned a total of {total_stars} this week!")
                sleep(self.sleep_time * 2)
                if total_stars == 15:
                    self.achievement.unlock("Maximum stars achieved!")
                    self.log.log("Achievement unlocked: Best Barista To Ever Exist!") # Game ending Achievement
                if total_stars == 0:
                    self.achievement.unlock("Wow, you did not earn a single star...")
                    self.log.log("Achievement unlocked: How do you manage to not get a single star...? LOSER! Get back on the streets!") # Game ending Achievement
            sleep(self.sleep_time * 2)
            self.day += 1  # proceed to next day
        self.day = 1
        self.__running = False

    def continue_game(self):
        """This method allows the user to simply continue on."""
        print("You continue working...\n")

        # testing achievements
        self.achievement.unlock("You're a hard worker!")
        self.achievements += 1
        if self.interact:
            self.long += 1
        self.update()
