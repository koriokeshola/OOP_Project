class Loggable:
    def __init__(self):
        self._logs = [] #creates private list to store log messages

    #getter for private logs list
    #is read-only access to the logs outside the class
    @property
    def logs(self):
        return self._logs

    def log(self, message: str):
        self._logs.append(message) #adds a new message to the logs list

    def save_logs_to_file(self, filename):
        #saves current logs to a specified file
        f = open(filename, 'w') #opens file in write mode
        for log in self._logs:
            f.write(log + '\n') #writes each log entry, then adds a newline
        f.close() #closes file after writing
        print(f"Logs saved to {filename}") #prints out message to confirm the save
