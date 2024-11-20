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
                self.running = False
            elif player_input.lower() == "s":
                self.start_game()
            elif player_input.lower() == "r":
                self.rules()
        else:
            """The update method waits for player input and responds to their
            choice to continue the game or quit."""
            player_input = input("Press 'c' to continue or 'q' to quit: ")
            if player_input.lower() == "q":
                # we exit the game running loop by setting this flag variable
                # to False
                self.running = False
            elif player_input.lower() == "c": # allows the user to choose to continue the game
                return

    def start_game(self):
        """The start_game method introduces the player to the mystery case and
        sets the scene."""

        print("\nYou find yourself in the opulent drawing room of a grand "
              "mansion. \nThe walls are huge and the floor is so clear you could see \n"
              "your face in it. \"This place looks quite expensive\" you tell yourself briefly."
              " \nAs the famous detective, you're here to solve the "
              "mysterious case of...\n'The Missing Diamond Necklace!'.\n"
              "Put your great detective skills to the test and unveil the truth about \n"
              "what has happened to this necklace!")

        # allows the user to input whichever door they wish to go through
        door_choice = int(input("Please choose Door One or Door Two [1 or 2]: "))

        # displays the result of going through door one
        if door_choice == 1:
            print("\nYou walk into Door One and you look around a bit. \n"
                  "You stumble on a jewelry box hidden under the table!")
            # sets the start variable to true so the update function will run correctly
            self.start = True

            # gives the user a chance to continue or leave the game
            self.update()

            # displays the continued monologue
            print("\nYou pick up the jewelry box and open it. \nYou find loads of "
                  "different expensive necklaces and earrings \nbut not the one you're looking for."
                  "\nYou decide to keep the box with you and continue heading forward."
                  "\nYou stumble on two more doors.!")

            # allows the user to input whichever door they wish to go through
            door_choice = int(input("Head through Door One or Door Two [1 or 2]: "))

            # depending on whichever door the user has chosen, a different result is displayed
            if door_choice == 1:
                print("\nYou walk into Door One and find an empty room :(\n"
                      "You decide to walk back to the drawing room to search.")
            elif door_choice == 2:
                print("\nYou walk into Door Two and have found a pearl "
                      "from a piece of jewelry!")
            # sets the start variable to true so the update function will run correctly
            self.update()

        # displays the result of going through door two
        elif door_choice == 2:
            print("\nYou walk into Door Two and notice you have found a \n"
                  "metal detector!")

            # sets the start variable to true so the update function will run correctly
            self.start = True

            # sets the start variable to true so the update function will run correctly
            self.update()

            print("\nYou pick up the metal detector and keep it with you as it could be useful to "
                  "\nfind the necklace. You continue to head forward."
                  "\nYou stumble on two more doors.!")

            # allows the user to input whichever door they wish to go through
            door_choice = int(input("Head through Door One or Door Two [1 or 2]: "))

            # depending on whichever door the user has chosen, a different result is displayed
            if door_choice == 1:
                print("\nYou walk into Door One and find a room covered top to bottom in cloths\n"
                      "You decide to use the metal detector you acquired to help hear if "
                      "\nthere is anything under the cloths.")
            elif door_choice == 2:
                print("\nYou walk into Door Two and have found the room where all the drawing"
                      " materials are kept!")

            # sets the start variable to true so the update function will run correctly
            self.update()




# runs the game from the Game function
if __name__ == "__main__":
    game = Game()
    game.run()
