# salesman_ag
M2 Project - Solving the travelling salesman using a genetic algorithm


# Croisement des enfants

## Crossover

Crossover 1 point => On met 1 point qui marque la séparation entre les 2 parents
Crossover 2 point => Pareil avec 2 points
Crossover Uniforme => Génère un masque qui donne la même proportion entre les parents

=> Pas Optimal pour TSP

https://tel.archives-ouvertes.fr/tel-00126292/document



# Truc à essayer

* [X] Taille de population de 2 * V ou 8 * V où V est le nombre de ville
* [X] Génération de la population avec une méthode heuristique
* [X] Méthode de sélection basé sur la roulette.
* [X] Opérateur de croisement edrx avec une probabilité de 1.
* [X] Opérateur de mutation im avec Pm = 0.9
* [X] Méthode d'insertion élististe.

* [ ] Ajouter la gestion de CSV
* [ ] Ajouter l'interface graphique
* [ ] Faire un main de qualité
* [ ] Ajouter 2-opt

# Seed 1

Meilleur route => 3970.0 "Ordre: 8, 6, 0, 9, 7, 5, 4, 3, 2, 1"

5 => 1436
graph_20 => 2815.
graph_200 => 7000
