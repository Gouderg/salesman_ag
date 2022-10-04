from math import sqrt

class Lieu:
    
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def distance(self, x2, y2):
        return int(sqrt((self.x - self.y)**2 + (x2 - y2)**2))