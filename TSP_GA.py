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

    def calculate_fitness(self, graph, best):
        a = [1/graph.calcul_distance_route(best[f]) for f in range(len(best))]
        self.fitness = [a[i]/sum(a) for i in range(len(a))]

    def selectionParents(self, graph):

        # Mise á jour des distances.
        for i in range(0, len(self.routes)):
            self.routes[i].distance = graph.calcul_distance_route(self.routes[i])

        # Sélection des NB_PARENTS meilleurs parents.    
        best = sorted(self.routes)[::-1][:min(NB_PARENTS, NB_POPULATION)]

        # Création de la fitness des 10 meilleurs parents.
        self.calculate_fitness(graph, best)

        # Choix des parents
        self.parents = [random.choices(best, weights=self.fitness, k=2) for i in range(NB_POPULATION//2)]

    def reproduction(self, graph):

        while len(self.enfants) != NB_POPULATION - NB_PARENTS:

            self.crossover()

            self.mutation()


            self.enfants.append()

    def crossover(self):
        pass

    def muter(self):
        pass
    
    def reset(self):
        self.routes = self.enfants + self.parents
        self.enfants, self.parents, self.fitness = None, None, None


if __name__ == "__main__":
    g = Graph()

    algo = TSP_GA()

    # On génère une population de route.
    algo.generate_routes(g)
    
    # On itère un certain nombre de fois
    for ite in range(NB_ITERATION):

        # Sélection des parents.
        algo.selectionParents(g)

        # Reproduction.
        algo.reproduction(g)

        # Création des enfants.
        algo.crossover()

        # Mutation des enfants.
        algo.muter()

        # Prération pour la prochaine itération.
        algo.reset()

        # Update de l'affichage graphique.

        break
    print()
