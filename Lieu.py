from math import sqrt

class Lieu:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # Renvoie la distance euclidienne entre 2 points.
    def distance(self, x2, y2) -> float:
        return sqrt((self.x - x2)**2 + (self.y - y2)**2)