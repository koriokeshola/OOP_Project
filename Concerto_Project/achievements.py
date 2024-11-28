# Program Description: A program used to create achievements which are
# unlockable based on players actions and counted throughout the game

from loggable import Loggable #importing Loggable class to handle log inputs

class Achievements:
    def __init__(self):
        self.unlocked_achievements = [] #stores unlocked achievements
        self.log = Loggable() #instance of loggable class

    def unlock(self, dialogue):
        #checks if achievement is already in the list. If not, it adds it to the list.
        if dialogue not in self.unlocked_achievements:
            self.unlocked_achievements.append(dialogue) #adds new achievement to the list
            print(f"Achievement Unlocked: {dialogue}") #prints out the achievement the player unlocked.
            self.log.log("Achievement Unlocked") #logs the event into the logs list
