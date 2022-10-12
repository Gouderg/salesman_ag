from tsp_graph_init import *
import numpy as np

class TSP_GA:
    def __init__(self) -> None:
        self.routes = []
        self.fitness = []
        self.parents, self.enfants = None, []

    def generation_population(self, graph) -> None:
        
        # Initialisation de la première personne.
        best_first_individu = Route([i for i in range(graph.nb_lieu)])

        # On itère sur chaque pour trouver la meilleure route pour commencer.
        for i in range(graph.nb_lieu):
            idx = 0
            tab, individu = [0 for j in range(graph.nb_lieu)], [0 for j in range(graph.nb_lieu)]
            
            while idx < graph.nb_lieu:

                tab = [graph.matrice_od[i, k] for k in range(0, graph.nb_lieu)]
                
                for k in range(0, idx):
                    tab[individu[k]] = -1

                save_i, save_v = 100000, 100000
                for index, value in enumerate(tab):
                    if value != -1 and value < save_v:
                        save_i, save_v = index, value

                individu[idx] = save_i
                idx += 1
            
            if graph.calcul_distance_route(individu) < graph.calcul_distance_route(best_first_individu):
                best_first_individu = individu

        self.routes.append(Route(best_first_individu))

        # Génération du reste de la population à partir de la première personne.
        cpt = 0
        while cpt < NB_POPULATION - 1:
            new_child = self.mutation_inverse(graph, self.routes[0])
            if new_child not in self.routes:
                self.routes.append(new_child)
                cpt += 1

    def mutation_inverse(self, graph, route) -> Route:
        cp = Route(route.ordre.copy())
        a, b = np.random.randint(0, graph.nb_lieu, 2)
        cp[a], cp[b] = cp[b], cp[a]        
        return cp

    def heuristique_2_opt(self, graph, route) -> Route:

        new_route = Route([])

        for i in range(1, len(route.ordre)-2):
            for j in range(i+1, len(route.ordre)):
                new_route.ordre = route[0:i] + route[j:-len(route)+i-1:-1] + route[j+1:len(route)]
                new_distance = graph.calcul_distance_route(new_route)

                if new_distance < graph.calcul_distance_route(route):
                    route.ordre = new_route.ordre.copy()

        return route

    def calculate_fitness(self, graph) -> None:
        a = [1/graph.calcul_distance_route(f) for f in self.routes]
        self.fitness = [a[i]/sum(a) for i in range(len(a))]

    def croisement_recombinaison_arc(self, graph, papa, maman) -> Route:

        # Création du tableau de voisinage.
        tableau_voisinage = {}
        for i in range(graph.nb_lieu):
            a, b = papa.ordre.index(i), maman.ordre.index(i)
            tableau_voisinage[i] = list(set([papa[(a-1)%graph.nb_lieu], papa[(a+1)%graph.nb_lieu], maman[(b-1)%graph.nb_lieu], maman[(b+1)%graph.nb_lieu]]))

        # On crée un tableau avec toutes les valeurs
        choix = [i for i in range(graph.nb_lieu)]

        # On cherche la première valeur.
        pos = random.choice(choix)

        # On ajoute le premier élément dans bebe.
        bebe = Route([])
        bebe.ordre.append(pos)
        choix.remove(pos)

        while len(bebe) < graph.nb_lieu:

            # On met à jour le tableau de voisinage.
            for key in tableau_voisinage:
                if pos in tableau_voisinage[key]:
                    tableau_voisinage[key].remove(pos)


            # Parmi tous les voisins de pos, on cherche celui qui a le moins de voisins.
            nb_voisins = [len(tableau_voisinage[elt]) for elt in tableau_voisinage[pos]]

            # S'ils ont tous le même nombre de voisins, on prends 1 au hasard.
            if len(nb_voisins) == 0 or min(nb_voisins) == max(nb_voisins):
                pos = random.choice(choix)
            else:
                pos = tableau_voisinage[pos][nb_voisins.index(min(nb_voisins))]

            # On met à jour notre enfant.
            bebe.addValue(pos)
            choix.remove(pos)

        return bebe


    def reproduction(self, graph) -> None:
        # Compteur pour comptabiliser les erreurs (Sortir s'il n'y a pu de possibilités).
        erreur = 0

        # On génère les scores d'adaptabilités de chaque individu de la population.
        self.calculate_fitness(graph)

        # On génère 70 % d'enfants et le reste de la population sera composés de parents.
        while len(self.enfants) != int(NB_POPULATION * PROP_ENFANTS):

            # On choisit 2 parents parmi les routes.
            papa, maman = random.choices(self.routes, weights=self.fitness, k=2)
             
            # On effectue le croisement des gènes.
            bebe = self.croisement_recombinaison_arc(graph, papa, maman)


            # On effectue la mutation avec une certaine probabilité.
            if random.choices([True, False], weights=[0.9, 0.1]):
                # bebe = self.mutation_inverse(graph, bebe)
                bebe = self.heuristique_2_opt(graph, bebe)


            # On gère le cas où on ne trouve plus de nouvel enfant.
            if bebe not in self.enfants:
                self.enfants.append(bebe)
                erreur = 0
            else:
                erreur += 1

            if erreur == 5:
                print("Impossible de trouver un nouvel enfant.")
                return -1
        
        self.parents = sorted(zip(self.fitness, self.routes))
        self.routes = self.enfants + [self.parents[i][1] for i in range(len(self.parents)-1, len(self.parents) - 1 -int(NB_POPULATION * PROP_PARENTS), -1)]

    
    def reset(self) -> None:
        self.enfants, self.parents, self.fitness = [], [], []

    def find_best_move(self, graph) -> tuple:
        best_move = 0
        r = Route([])
        for elt in self.routes:
            d_temp = graph.calcul_distance_route(elt)
            if d_temp < best_move or best_move == 0:
                best_move, r = d_temp, elt
        return best_move, r

    def main(self, graph) -> tuple:
        d, r = None, None

        # On génère une population de route.
        self.generation_population(graph)
        
        # On itère un certain nombre de fois
        for ite in range(NB_ITERATION):

            # Reproduction.
            if self.reproduction(graph) == -1: break

            # Préparation pour la prochaine itération.
            self.reset()

            # Meilleur coup de l'itération.
            d, r = self.find_best_move(graph)

            # Update de l'affichage graphique.

        return r, d

if __name__ == "__main__":
    csv_file = "csv/graph_20.csv"
    csv_matrice_od = "csv/matrice_od_a_plat_m.csv"
    # csv_opt = "csv/a280.opt.tour.csv"
    csv_opt = None
    # csv_file = None
    csv_matrice_od = None
    

    # Init Performance object.
    g = Graph(csv_file, csv_matrice_od)
    algo = TSP_GA()

    print(algo.main(g))


