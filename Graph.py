from constante import LARGEUR, HAUTEUR, NB_LIEUX
from Lieu import Lieu

import random
import numpy as np
import pandas as pd

class Graph:
    
    def __init__(self, csvNameLieux = None, csvMatrice = None) -> None:
        
        # Déclation des variables.
        self.list_lieu = []
        self.nb_lieu = NB_LIEUX
    
        self.charger_graph(csvNameLieux)
        self.matrice_od = np.zeros((self.nb_lieu, self.nb_lieu))
        self.charger_matrice_od(csvMatrice)
    
    def calcul_distance_route(self, ordre) -> float:
        return sum([self.matrice_od[ordre[i], ordre[i+1]] for i in range(0, self.nb_lieu-1)] + [self.matrice_od[ordre[self.nb_lieu-1], ordre[0]]])

    
    # Trouve le plus proche voisin en utilisant la transposé de la matrice pour permettre de travailler sur la ligne.
    def plus_proche_voisin(self, index, k_plus_proche = 0) -> int:

        # On récupère la ligne de la transposé et on la trie.
        trans = np.array(sorted(self.matrice_od.T[index]))

        # On enlève temporairement les valeurs négatives.
        without_negative = trans[len(trans) - sum(1 * (trans > 0)):]

        # On récupère la valeur la plus petite.
        val = without_negative[k_plus_proche]
   
        # On cherche l'indice de la valeur.
        ind = np.where(self.matrice_od.T[index] == val)[0][0]

        return ind

    
    def charger_graph(self, csvName=None) -> None:
        
        if csvName is None:
            random.seed(1)
            for i in range(self.nb_lieu):
                self.list_lieu.append(Lieu(random.randint(0, LARGEUR), random.randint(0, HAUTEUR)))
        
        else:
            df = pd.read_csv(csvName, sep=",", header=None)
            min_x, min_y, max_x, max_y = min(list(df[0])), min(list(df[1])), max(list(df[0])), max(list(df[1]))

            for x, y in zip(list(df[0]), list(df[1])):
                if max_y > HAUTEUR or max_x > LARGEUR:
                    self.list_lieu.append(Lieu((x - min_x) / (max_x - min_x) * LARGEUR, (y - min_y) / (max_y - min_y) * HAUTEUR))
                else:
                    self.list_lieu.append(Lieu(x, y))

            
            self.nb_lieu = len(self.list_lieu)


    def charger_matrice_od(self, csvName=None) -> None:

        if csvName is None:
            for i in range(0, self.nb_lieu):
                for j in range(0, i):
                    l = self.list_lieu[j]
                    self.matrice_od[i, j] = self.list_lieu[i].distance(l.x, l.y)
                    self.matrice_od[j, i] = self.list_lieu[i].distance(l.x, l.y)

        else:
            df = pd.read_csv(csvName, sep=",", header=None)
            for i, j, val in zip(list(df[0]), list(df[1]), list(df[2])):
                self.matrice_od[i-1, j-1] = val

