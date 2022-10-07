from constante import LARGEUR, HAUTEUR, NB_LIEUX
from Lieu import Lieu

import random
import numpy as np

class Graph:
    
    def __init__(self):
        
        # Déclation des variables.
        self.list_lieu = []
        self.matrice_od = np.zeros((NB_LIEUX, NB_LIEUX))
    
        self.charger_graph()
        self.charger_matrice_od()
    
    def calcul_distance_route(self, ordre):
        return sum([self.matrice_od[ordre[i], ordre[i+1]] for i in range(0, len(ordre)-1)])

    
    # Trouve le plus proche voisin en utilisant la transposé de la matrice pour permettre de travailler sur la ligne.
    def plus_proche_voisin(self, index, k_plus_proche = 0):

        # On récupère la ligne de la transposé et on la trie.
        trans = np.array(sorted(self.matrice_od.T[index]))

        # On enlève temporairement les valeurs négatives.
        without_negative = trans[len(trans) - sum(1 * (trans > 0)):]

        # On récupère la valeur la plus petite.
        val = without_negative[k_plus_proche]
   
        # On cherche l'indice de la valeur et on la convertie en lettre.
        ind = np.where(self.matrice_od.T[index] == val)[0][0]

        return ind

    
    def charger_graph(self, isCsv=False):
        
        if not isCsv:
            random.seed(1)
            for i in range(NB_LIEUX):
                self.list_lieu.append(Lieu(random.randint(0, LARGEUR), random.randint(0, HAUTEUR), chr(ord('A') + i)))

    def charger_matrice_od(self, isCsv=False):

        if not isCsv:
            for i in range(NB_LIEUX):
                for j in range(i):
                    l = self.list_lieu[j]
                    self.matrice_od[i, j] = self.list_lieu[i].distance(l.x, l.y)
                    self.matrice_od[j, i] = self.list_lieu[i].distance(l.x, l.y) * 2

