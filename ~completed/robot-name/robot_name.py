import random as rd
from string import ascii_uppercase as ascu

class Robot:
    def __init__(self):
        self.name = self.random_name()

    def random_name(self):
        rd.seed()
        name = ''
        for i in (rd.choices(ascu, k=2)) + (list(str(rd.randint(000, 999)).zfill(3))):
            name += i
        return name

    def reset(self):
        self.name = self.random_name()
