from tsp_graph_init import *
from tkinter import *
import time
import numpy as np
from TSP_GA import TSP_GA

def takeDistance(element):
    return element[0]

def main():
    best_routes = []

    graph = Graph()
    algo = TSP_GA()
    algo.generation_population(graph)


    app = Affichage(graph.list_lieu)

    for i in range(1000):

        # Reproduction.
        if algo.reproduction(graph) == -1: break

        # Prération pour la prochaine itération.
        algo.reset()

        # Meilleur coup de l'itération.
        d, r = algo.find_best_move(graph)

        if len(best_routes) == 0:
            best_routes.append((d, r))
        else:
            if d < best_routes[0][0]:
                best_routes.append((d, r))
                best_routes.sort(reverse=True, key=takeDistance)
                if len(best_routes) > 10:
                    best_routes.pop(0)

        # Update de l'affichage graphique.
        for j in range(9):
            app.draw_path(graph.list_lieu[r[j]], graph.list_lieu[r[j+1]])

        for k in range(len(best_routes)):
            for l in range(9):
                app.draw_path_color(graph.list_lieu[best_routes[k][1][l]], graph.list_lieu[best_routes[k][1][l+1]])


        #print(i, d, r)
        app.draw(i, best_routes[len(best_routes)-1])
        #app.draw(str(i), r.ordre)

        app.update()
        app.update_idletasks()

        app.reset_paths()


if __name__ == "__main__":
    main()
