from constante import LARGEUR, HAUTEUR, NB_LIEUX
from Lieu import Lieu

from random import randint
import numpy as np

class Graph:
    
    def __init__(self):
        self.list_lieu = {}

        self.matrice_od = np.zeros((NB_LIEUX, NB_LIEUX))
    
    
    def calcul_matrice_od(self):
        pass

    
    def plus_proche_voisin(self):
        plus_proche_voisin = None

        return plus_proche_voisin
    
    def charger_graph(self, isCsv=False):
        
        if not isCsv:
            name = 'A'
            for i in range(NB_LIEUX):
                
                # On crée le lieu.
                l = Lieu(randint(0, 800), randint(0, 800), name)

                # On l'ajoute à la liste.
                self.list_lieu[name] = l

                # On augmente le nom.
                name = chr(ord(name) + 1)
        else:
            pass


    def charger_matrice_od(self, isCsv=False):

        if not isCsv:
            for i in range(NB_LIEUX):
                for j in range(NB_LIEUX):
                    if i == j:
                        continue
                    l = self.list_lieu[chr(ord('A') + j)]
                    self.matrice_od[i, j] = self.list_lieu[chr(ord('A') + i)].distance(l.x, l.y)
