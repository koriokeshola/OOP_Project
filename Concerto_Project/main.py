################################################################################
# CMPU 2016 OOP – TU857/2 - Semester 1 Assignment.
# Group: Concero
# Members:
# 1. Blessing Ugochukwu (student ID: C23342083).
# 2. Renée Low (student ID: C23321923).
# 3. Kori Okeshola (student ID: C23401212).
# 4. Bouthayna Metarfi (student ID: C23306091).
# 5. Bartosz (student ID: C23398751).
# 6. Seema Alazhari (student ID: C23405732).
# Date: November 26, 2024.
#
# Game Expansion Explanation:
# In our project, we created a game with a café theme where players are a barista in the café
# and interacts with customers and takes their orders, then makes the customer's order by choosing
# the available options. We've implemented an achhievemnts that players can unlock,
# levels that unlocks new menus, a system to log the player interactions and a star system
# where players can earn stars based on if they've made a customer's order correctly.
#
# File Structure:
# - main_game.py: The main game script.
# - achievements.py: Module for handling achievements.
# - makeDrink.py: Module for making drinks.
# - game.py: Module containing game content.
# - loggable.py: Module for logging interactions.
# - characters.py: Module containing character player interacts with.
# - design.py: Module containing design for the days.
# - reviews.py: Module containing a hidden reviews list from customers.
#
# Running the Game:
# - To play "The Golden Café" with our expansions, run the "main_game.py" file.
# - ensure that the modules for "achievements.py" "game.py", "loggable.py", "makeDrink.py", "character.py" and "design.py
# are there for full functionality of the game.

# Enjoy the game and have fun being a barista.
################################################################################
from game import Game

# runs the game from the Game function
if __name__ == "__main__":
    game = Game()
    game.run()

    print("\nGame Logs:")
    for log in game.log.logs:
        print(log)
