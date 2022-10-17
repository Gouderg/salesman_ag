from constante import LARGEUR, HAUTEUR, NB_LIEUX
from Lieu import Lieu

import random
import numpy as np
import pandas as pd

class Graph:
    
    def __init__(self, csvNameLieux = None, csvMatrice = None, nb_lieux=NB_LIEUX) -> None:
        
        # Déclation des variables.
        self.list_lieu = []
        self.nb_lieu = nb_lieux
    
        self.charger_graph(csvNameLieux)
        self.matrice_od = np.zeros((self.nb_lieu, self.nb_lieu))
        self.charger_matrice_od(csvMatrice)
    
    # Calcul de la distance entre les différents passés en paramètres.
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

    # Charge soit un fichier CSV, soit il génère des nombres aléatoires.
    def charger_graph(self, csvName=None) -> None:
        
        if csvName is None:
            random.seed(1)
            for i in range(self.nb_lieu):
                self.list_lieu.append(Lieu(random.randint(0, LARGEUR), random.randint(0, HAUTEUR)))
        
        else:
            df = pd.read_csv(csvName, sep=",", header=None)

            for x, y in zip(list(df[0]), list(df[1])):
                self.list_lieu.append(Lieu(x, y))

            
            self.nb_lieu = len(self.list_lieu)

    # Si un fichier csv est passé, il le charge, sinon il crée une matrice_od avec la distance euclidienne.
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

