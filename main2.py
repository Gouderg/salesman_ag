from tsp_graph_init import *
import time
import numpy as np
from TSP_GA import TSP_GA

def main():
    g = Graph()
    algo = TSP_GA(g)
    algo.generate_routes()


if __name__ == "__main__":
    main()
