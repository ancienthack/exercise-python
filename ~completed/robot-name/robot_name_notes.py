import random as rd
from string import ascii_uppercase as ascu

class Robot:
    def __init__(self):
        self.name = None

    def name(self):
        # print(rd.choices(ascu, k=2))
        # print(list(str(rd.randint(000, 999))))
        # print((rd.choices(ascu, k=2)) + (list(str(rd.randint(000, 999)))))
        rd.seed()
        name = ''
        for i in (rd.choices(ascu, k=2)) + (list(str(rd.randint(000, 999)))):
            # self.name += i
            name += i
        return name

    def reset(self):
        self.name = self.name()

robot = Robot()
name = robot.name
print(name)