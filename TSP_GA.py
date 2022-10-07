from tsp_graph_init import *


class TSP_GA:
    def __init__(self):
        self.routes = []
        self.fitness = []
        self.parents = None


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

    def calculate_fitness(self, graph):
        a = [1/graph.calcul_distance_route(self.routes[f]) for f in range(NB_LIEUX)]
        self.fitness = [a[i]/sum(a) for i in range(NB_LIEUX)]

    def selectionParents(self):
        self.parents = [random.choices(self.routes, weights=self.fitness, k=2) for i in range(NB_POPULATION//2)]

    def crossover(self):
        self.enfants = 0

    def muter(self):
        self.enfants = 0
    
    def reset(self):
        self.routes = self.enfants
        self.enfants, self.parents, self.fitness = None, None, None


if __name__ == "__main__":
    g = Graph()

    algo = TSP_GA()

    # On génère une population de route.
    algo.generate_routes(g)
    
    # On itère un certain nombre de fois
    for ite in range(NB_ITERATION):

        # Calcul du fitness de chaque Route et on normalise.
        algo.calculate_fitness(g)

        # Sélection des parents.
        algo.selectionParents()

        # Création des enfants.
        algo.crossover()

        # Mutation des enfants.
        algo.muter()

        # Prération pour la prochaine itération.
        algo.reset()

        # Update de l'affichage graphique.

        break
    print()
