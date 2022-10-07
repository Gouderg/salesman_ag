from tsp_graph_init import *
import time
import numpy as np

# Création du graph.
graph = Graph()

print(graph.matrice_od)
route = Route()
route.ordre = list(graph.list_lieu)
print(route)
route.addValue("F")


print("Distance de la route: ", graph.calcul_distance_route(route.ordre))
print("Plus proche voisin de D: ", graph.plus_proche_voisin("D"))



# # Création de l'affichage.
# app = Affichage(graph.list_lieu)

# Boucle de mise en service.
# for i in range(1000):
#     app.draw(i, ['a', 'b'])
#     app.update()
#     app.update_idletasks()
#     time.sleep(0.02)