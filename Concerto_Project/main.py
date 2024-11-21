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
from game import Game

# runs the game from the Game function
if __name__ == "__main__":
    game = Game()
    game.run()

    print("\nGame Logs:")
    for log in game.log.logs:
        print(log)