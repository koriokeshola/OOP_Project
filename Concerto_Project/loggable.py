# Program Description: This program contains the logic for game logging.
# Includes a private log getter, and methods for adding and saving logs.
# The complete list of logs is displayed from main when game is finished.

class Loggable:
    def __init__(self):
        self._logs = [] # creates private list to store log messages

    # Getter for private logs list
    # Provides read-only access for the logs outside the class
    @property
    def logs(self):
        return self._logs

    def log(self, message: str):
        self._logs.append(message) # Adds a new message to the logs list

    def save_logs_to_file(self, filename):
        # Saves current logs to a specified file
        try: # Use try-except block to handle potential errors
            with open(filename, 'w') as file: # open and then close when finished
                for log in self._logs:
                    file.write(log + '\n') # Writes each log entry, then adds a newline
            print(f"Logs saved to {filename}") # Prints out message to confirm the save
        except Exception as e: # exception for unexpected error
            print(f"Error: {e}. An unexpected error occurred while saving logs.")
            self.log.log(f"Unexpected Error: {e}")
