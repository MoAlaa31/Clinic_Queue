import random
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.age = random.randrange(20,61)

    def getStamp(self):
        return self.timestamp

    def getpatient(self):
        return self.age

    def waitTime(self, currenttime):
        return currenttime - self.timestamp