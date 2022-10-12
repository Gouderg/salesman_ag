from tsp_graph_init import *
import time
import numpy as np


# Création du graph.
graph = Graph()

new_route = Route([])
route = Route([i for i in range(10)])
print(route)
i = 2
j = 4
new_route.ordre = route[0:i] + route[j:-len(route)+i-1:-1] + route[j+1:len(route)]
print(new_route)
# tsp.croisement_recombinaison_arc(papa, maman)

# print(d, r)
# for elt in tsp.routes:
#     print(elt, graph.calcul_distance_route(elt))

# route = Route()
# route.ordre = [i for i in range(NB_LIEUX)]
# print(route)
# route.addValue(2)


# print("Distance de la route: ", graph.calcul_distance_route(route.ordre))
# print("Plus proche voisin de D: ", graph.plus_proche_voisin(2))


# # Création de l'affichage.
# app = Affichage(graph.list_lieu)

# # Boucle de mise en service.
# for i in range(1000):
#     app.draw(i, ['a', 'b'])
#     app.update()
#     app.update_idletasks()
#     time.sleep(0.02)