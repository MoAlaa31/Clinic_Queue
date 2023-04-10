class Clinic:
    def __init__(self, patientsrate):
        self.w8ingtimerate = patientsrate
        self.currentpatient = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentpatient != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining == 0:
                self.currentpatient = None

    def busy(self):
        if self.currentpatient != None:
            return True
        else :
            return False

    def startNext(self,newpatientage):
        self.currentpatient = newpatientage
        self.timeRemaining = newpatientage.getpatient() * 60/self.w8ingtimerate