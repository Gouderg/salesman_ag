from tsp_graph_init import *


class TSP_GA:
    def __init__(self):
        self.routes = []
        self.fitness = []


    def generate_routes(self, graph):
        for j in range(NB_POPULATION):
            villes = [i for i in range(NB_LIEUX)]
            route = Route()
            for i in range(NB_LIEUX):
                a = random.choice(villes)
                route.addValue(a)
                villes.remove(a)
            route.addValue(route[0])
            self.routes.append(route)

    def calculate_fitness(self, graph, index):
        return 1/graph.calcul_distance_route(self.routes[index])

    def main(self):
        print("Launch application.")


if __name__ == "__main__":
    g = Graph()

    algo = TSP_GA()

    # On génère une population de route.
    algo.generate_routes(g)
    
    # On itère un certain nombre de fois
    for ite in range(NB_ITERATION):

        # Calcul du fitness de chaque Route et on normalise.
        algo.fitness = [algo.calculate_fitness(g, f) for f in range(NB_LIEUX)]
        algo.fitness = [algo.fitness[i]/sum(algo.fitness) for i in range(NB_LIEUX)]

        print(algo.fitness)

        break
    print()
