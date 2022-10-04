from tsp_graph_init import *
import time

# Création du graph.
graph = Graph()
graph.charger_graph()
graph.charger_matrice_od()

route = Route()
route.ordre = ["A", "B", "C", "D", "A", "C"]

print(graph.calcul_distance_route(route.ordre))
# # Création de l'affichage.
# app = Affichage(graph.list_lieu)

# Boucle de mise en service.
# for i in range(1000):
#     app.draw(i, ['a', 'b'])
#     app.update()
#     app.update_idletasks()
#     time.sleep(0.02)