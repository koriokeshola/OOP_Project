class Loggable:
    def __init__(self):
        self._logs = []

    @property
    def logs(self):
        return self._logs

    def log(self, message: str):
        self._logs.append(message)

    def save_logs_to_file(self, filename):
        f = open(filename, 'w')
        for log in self._logs:
            f.write(log + '\n')
        f.close()
        print(f"Logs saved to {filename}")
