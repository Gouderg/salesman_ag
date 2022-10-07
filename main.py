from tsp_graph_init import *
import time

# Création du graph.
graph = Graph()

route = Route()
route.ordre = ["A", "B", "C", "D", "A", "C"]
print(len(route))
print(route[2])
route.addValue("F")
print(route)

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