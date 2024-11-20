# CMPU 2016 Object-Oriented Programming
# TU857-2
# 26/09/24, Semester 1: Python with Blessing Ugochukwu, C23342083
#
# Mystery Adventure Game - Week 1 Lab Template
# Introduction to Mystery Adventure Game Development
# Setting up the initial game environment and introduction scene
#
# Learning objectives lab week 1:
# 1. Understand Basic Python Programming:
#    - Familiarize yourself with the structure of a Python script.
#    - Identify the role of classes and methods in Python code.
# 2. Handle User Input:
#    - Learn to use the input() function to receive user input.
#    - Practice capturing and processing user choices and responses.
# 3. Apply If-Else Statements:
#    - Understand the concept of conditional statements.
#    - Learn to use if-else statements to control program flow based on
#    conditions.
# 4. Enhance User Experience:
#    - Explore techniques to make user interactions more engaging and immersive.
#    - Learn to incorporate descriptive text and narrative elements into your
#    program.
# 5. Modify Menu Options Dynamically:
#    - Understand how to change menu options based on the game's state.
#    - Learn to dynamically adjust user choices to match the game's progression.

from abc import ABC, abstractmethod

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

class Recipes:
    def __init__(self, size, milk, sugar, temp, ice):
        self.size = size # s, m or l
        self.milk = milk # yes or no
        self.sugar = sugar # 1, 2, or 3 spoons
        self.temp = temp # hot, cold
        self.ice = ice # yes, no, or extra
        
    def coffee_options(self):
        print()
        
    def tea_options(self):
        print()
        
    def boba_options(self):
        print()
        

class Game:
    """The Game class is set up to manage the game's behavior."""

    def __init__(self):
        # self.running is an instance variable within the Game class
        # This means that when an instance of the Game class is created,
        # the game loop will start running by default as it is set to True.
        self.running = True
        self.start = False
        self.log = Loggable()

    def run(self):
        """The run method starts the game loop and provides an introduction to
        the game."""

        print("You're stumbling around in the cold, cant feel your face... "
              "\nA strange figure approaches. you cant see in the harsh conditions"
              "\nHe extends out his hand.. you reach out"
              "\nHe offers you a chance to redeem yourself, a nice job in a cozy cafe"
              "\nYou accept.. reluctantly"
              "\nNow your journey begins...")
        print("\t\t\tG O L D E N   C A F É"
              "\n*******************************************"
              "\n|                                         |"
              "\n|     Serving Coffee, Tea, and Boba!      |"
              "\n|                                         |"
              "\n*******************************************\n")
        print("Now that you have started your job, you will have to satisfy customers everyday")


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
        if self.start == False:
            player_input = input("Press 'q' to quit, 'r' for rules or 's' to start: ")
            if player_input.lower() == "q":
                # we exit the game running loop by setting this flag variable
                # to False
                self.log.log("Player quits the game")
                self.running = False
            elif player_input.lower() == "s":
                self.game_started = True
                self.start_game()
                self.log.log("Player starts the game")
            elif player_input.lower() == "r":
                self.rules()
                self.log.log("Player checks the rules")
        else: #if user chooses to continue they get more options
            player_input = input("Press 'q' to quit, 'c' to continue, "
                                 "'i' to interact,"
                                 "'m' to make drink")
            if player_input.lower() == "q": #quits game
                self.running = False
                self.log.log("Player quits the game")  
            elif player_input.lower() == "c": #continues game
                self.log.log("Player continued working")  
                self.continue_game()
            elif player_input.lower() == "i": #interacts with customer
                self.log.log("Player talks to the customer")
                self.interact_with_customers()
            elif player_input.lower() == "m": #chooses a door
                self.log.log("Player chooses to make a drink")
                self.make_drink()

    def start_game(self):
        """The start_game method introduces the player to the mystery case and
        sets the scene."""

        print("\nGame intro")

    def make_drink(self): #method for choosing a door
        self.drink = input("What drinm do you want to make. \n"
                                 "1. Coffee\n"
                                 "2. Tea\n"
                                 "3. Boba\n"
                                 "Enter the number of the drink you want to make: ")
        if self.drink == "1":
            print("placeholder")
        elif self.drink == "2":
            print("placeholder")
        elif self.door_choice == "3":
            print("place holder")

    def continue_game(self):
        print("You continue working...")
        self.log.log("Player continued working")

# runs the game from the Game function
if __name__ == "__main__":
    game = Game()
    game.run()

    print("\nGame Logs:")
    for log in game.log.logs:
        print(log)
