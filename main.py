from pythonds.basic.queue import Queue
from Printer import *
from task import *

import random
# def rem (que,rate):
#     age_sum = 0
#     for item in que.items:
#         age_sum += item.getpatient()
#     return age_sum


def simulation (numSeconds, doctorrate):
    Doctor = Clinic(doctorrate)
    clinicqueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if random.randrange(1, 361) == 360:
            task = Task(currentSecond)
            clinicqueue.enqueue(task)
        if(not Doctor.busy()) and (not clinicqueue.isEmpty()):
            nextpatient = clinicqueue.dequeue()
            waitingtimes.append(nextpatient.waitTime(currentSecond))
            Doctor.startNext(nextpatient)
        Doctor.tick()

    averageWait = sum(waitingtimes) // (len(waitingtimes) * 60)
    average_Wait = (sum(waitingtimes) // (len(waitingtimes))) % 60
    print("Average Wait", averageWait, "min", average_Wait, "sec", clinicqueue.size(), "patient remaining.")
    return averageWait


x = 0
for i in range(100):
    x += simulation(4 * 3600, 5) / 100
print(x)