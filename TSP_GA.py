from tsp_graph_init import *

class TSP_GA:
    def __init__(self):
        self.routes = []

    def generate_routes(self, graph):
        for j in range(NB_POPULATION):
            villes = list(graph.list_lieu)
            route = Route()
            for i in range(NB_LIEUX):
                a = random.choice(villes)
                route.addValue(a)
                villes.remove(a)
            self.routes.append(route)
        print(self.routes)

    def calculate_fitness(self, index, graph):
        return 1/graph.calcul_distance_route(self.routes[index])



    def main(self):
        print("Launch application.")


if __name__ == "__main__":
    g = Graph()

    algo = TSP_GA()
    algo.generate_routes(g)
    print(algo.calculate_fitness(0, g))
