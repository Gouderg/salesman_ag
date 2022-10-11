from tsp_graph_init import *
from TSP_GA import TSP_GA

import itertools
from tqdm import tqdm
import math
import multiprocessing as mp
import numpy as np
from time import sleep
from queue import Empty

NB_ESSAI = 30

class Performance:

    def __init__(self, g) -> None:
        
        self.graph = g

        # On récupère la meilleure solution.
        self.best_move = None
        self.best_distance = 0

        self.all_dist = []
        self.all_routes = []

    def find_best_path(self) -> None:
        print("On essaie de trouver le chemin exact le plus court (Lieux <= 10): ")
        if NB_LIEUX > 10: return # Too many possibilities.

        # Trouver la solution la plus optimisé.
        r = Route([i for i in range(NB_LIEUX)])
        d = self.graph.calcul_distance_route(r)

        # Fonction factorielle.
        factorielle = lambda n: n * factorielle(n-1) if n != 0 else 1

        for elt in tqdm(itertools.permutations(range(NB_LIEUX), NB_LIEUX), total=factorielle(NB_LIEUX)):
            d_temp = self.graph.calcul_distance_route(Route(elt))
            if d_temp < d:
                r = Route(elt)
                d = d_temp
        
        self.best_move = r
    
    # Méthode qui calcule l'erreur.
    def rmse(self, all_route, all_dist):
        

        mean = np.quantile(all_dist, 0.5)
        q1 = np.quantile(all_dist, 0.25)
        q3 = np.quantile(all_dist, 0.75)
        ecart_type = np.std(all_dist)
        
        rmse1, rmse2 = 0, 0
        for elt in all_dist:
            rmse1 += (elt - self.best_distance)**2 / NB_ESSAI
            rmse2 += (elt - mean)**2 / NB_ESSAI

        rmse1 = math.sqrt(rmse1)
        rmse2 = math.sqrt(rmse2 + (mean - self.best_distance)**2)


        print("RMSE1: ",round(rmse1, 2),", RMSE2: ",round(rmse2, 2),", Min: ",min(all_dist),", Max: ",max(all_dist))
        print("Moyenne: ", mean,", Q1: ", q1, ", Q3: ", q3, ", Ecart-type: ", round(ecart_type, 2))

def producer(queue, p):
    print("\nLa meilleure route est ",p.best_move," avec une distance de ", p.best_distance,".\n")

    print("On réalise une acquisition de", NB_ESSAI,"itérations.")
    print("Les paramètres sont:")
    print("- Population:",NB_POPULATION)
    print("- Nombre de lieux:", NB_LIEUX)
    print("- Nombre d'itérations:", NB_ITERATION)
    print(flush=True)

    for i in range(NB_ESSAI):
        queue.put(i)

    

def consumer(queue, p):

    while True:
        try:
            # Get the id of the iteration.
            id = queue.get(block=False)

            algo = TSP_GA()
            route, distance = algo.main(p.graph)

            all_dist.append(distance)
            all_route.append(route)

            print("Itération n° ",id,"\t Route: ",route,"\t Distance: ", distance, flush=True)

            queue.task_done()
        except Empty:
            sleep(0.5)
            break


if __name__ == "__main__":

    # Show the number of processor.
    print("Nombre de CPU:", mp.cpu_count(), ", le programme tourne sur", mp.cpu_count() - 2,"cpus")

    # Init Performance object.
    g = Graph()
    p = Performance(g)
    p.find_best_path()
    p.best_distance = g.calcul_distance_route(p.best_move)
    
    manager = mp.Manager()
    all_route = manager.list()
    all_dist = manager.list()

    # Init queue.
    queue = mp.JoinableQueue()

    # Producer process.
    producer_process = mp.Process(target=producer, args=(queue, p, ))
    producer_process.start()

    # Consummer process.
    for i in range(mp.cpu_count()-2):
        co = mp.Process(target=consumer, args=(queue, p, )).start()


    # Wait all process to finish.
    producer_process.join()

    # Wait consumer to finish.
    queue.join()

    p.rmse(all_route, all_dist)
