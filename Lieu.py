from math import sqrt

class Lieu:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, x2, y2) -> int:
        return int(sqrt((self.x - self.y)**2 + (x2 - y2)**2))