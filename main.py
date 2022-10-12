from tsp_graph_init import *
import time
import numpy as np
from Performance import Performance

# Création du graph.
graph = Graph()


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