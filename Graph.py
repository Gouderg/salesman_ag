import constante
from constante import LARGEUR, HAUTEUR, NB_LIEUX
from Lieu import Lieu

from random import randint
import numpy as np

class Graph:
    
    def __init__(self):
        
        # Déclation des variables.
        self.list_lieu = {}
        self.matrice_od = np.zeros((NB_LIEUX, NB_LIEUX))
    
        self.charger_graph()
        self.charger_matrice_od()
    
    def calcul_distance_route(self, ordre):
        return sum([self.matrice_od[ord(ordre[i])-65, ord(ordre[i+1])-65] for i in range(len(ordre)-1)])
    
    # Trouve le plus proche voisin en utilisant la transposé de la matrice pour permettre de travailler sur la ligne.
    def plus_proche_voisin(self, index):
        return chr(np.where(self.matrice_od.T[ord(index)-65] == sorted(self.matrice_od.T[ord(index)-65])[1])[0][0] + 65)
    
    def charger_graph(self, isCsv=False):
        
        if not isCsv:
            for i in range(NB_LIEUX):
                self.list_lieu[chr(ord('A') + i)] = Lieu(randint(0, constante.LARGEUR), randint(0, constante.HAUTEUR), chr(ord('A') + i))

    def charger_matrice_od(self, isCsv=False):

        if not isCsv:
            for i in range(NB_LIEUX):
                for j in range(i):
                    l = self.list_lieu[chr(ord('A') + j)]
                    self.matrice_od[i, j] = self.list_lieu[chr(ord('A') + i)].distance(l.x, l.y)
                    self.matrice_od[j, i] = self.list_lieu[chr(ord('A') + i)].distance(l.x, l.y) * 2

