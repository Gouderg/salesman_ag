from tsp_graph_init import *
import time
import numpy as np
from TSP_GA import TSP_GA

def main():
    g = Graph()
    algo = TSP_GA()
    algo.generate_routes(g)

    route_to_expose = algo.routes[0]

    app = Affichage(g.list_lieu)
    for i in range(1000):
        for j in range(9):
            app.draw_path(g.list_lieu[route_to_expose[j]], g.list_lieu[route_to_expose[j+1]])
        app.update()
        app.update_idletasks()
        time.sleep(0.02)


if __name__ == "__main__":
    main()
