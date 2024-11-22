from loggable import Loggable

class Achievements:
    def __init__(self):
        self.unlocked_achievements = []
        self.log = Loggable()

    def unlock(self, dialogue):
        #checks if achievement is already in the list. If not, it adds it to the list.
        if dialogue not in self.unlocked_achievements:
            self.unlocked_achievements.append(dialogue)
            print(f"Achievement Unlocked: {dialogue}") #prints out the achievement the player unlocked.
            self.log.log("Achievement Unlocked")
