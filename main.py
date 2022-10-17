import os
from pathlib import Path

from Performance import main_perf
from TSP_GA import main_tsp_ga


def parsearg():
    import argparse

    # On récupère les arguments de la ligne de commande.
    ap = argparse.ArgumentParser(description="TSP with Genetic Algorithm", epilog="Thanks to use it!")

    # Utilisation du mode graphique ou du mode performance.
    arg_input = ap.add_mutually_exclusive_group(required=True)
    arg_input.add_argument("-eperf", "--enable_performance_mode", action="store_true", help="Lance en mode performance")
    arg_input.add_argument("-egraph", "--enable_graphic_mode", action="store_true", help="Lance en mode graphique avec tkinter")

    # Nombre de CPU à utiliser en mode performance.
    ap.add_argument("-cpu", "--cpu_count", default=1, help="Nombre de CPU à utiliser en mode performance")

    # Nombre de lieux.
    ap.add_argument("-lieux", "--lieux_count", default=10, help="Nombre de lieux")

    # Chemin pour les différents csv.
    ap.add_argument("--name_csv", default="csv/graph_20.csv", help="Nom du fichier csv contenant les différents villes. Si None alors on génère les villes avec le nombre de lieux")
    ap.add_argument("--name_matrice", default=None, help="Charge une matrice_od si non renseigné alors génère la matrice od ")
    ap.add_argument("--name_csv_opt_tour", default=None, help="Charge un tour optimale sinon essaie de la calculer si le nombre de lieux <= 10.")

    return ap.parse_args()

def launch_app(arg):

    # On vérifie si les chemins d'accès aux fichiers sont bons.    
    csv_name = arg.name_csv if arg.name_csv is not None and os.path.isfile(Path(arg.name_csv)) else None
    name_matrice = arg.name_matrice if arg.name_matrice is not None and os.path.isfile(Path(arg.name_matrice)) else None
    name_csv_opt_tour = arg.name_csv_opt_tour if arg.name_csv_opt_tour is not None and os.path.isfile(Path(arg.name_csv_opt_tour)) else None

    cpu = int(arg.cpu_count)
    nb_lieu = int(arg.lieux_count)

    # Si Mode Performance.
    if arg.enable_performance_mode:
        main_perf(csv_name, name_matrice, name_csv_opt_tour, cpu, nb_lieu)


    # Si Mode Graphique.
    if arg.enable_graphic_mode:
        main_tsp_ga(csv_name, name_matrice, nb_lieu)


if __name__ == "__main__":
    arg = parsearg()
    launch_app(arg)
