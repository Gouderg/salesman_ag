from constante import *
from Graph import *
import tkinter as tk


class Affichage(tk.Tk):

    def __init__(self, graph) -> None:
        tk.Tk.__init__(self)

        # Crée le canvas.
        self.title("Salesman GA - Groupe 6")
        self.canvas = tk.Canvas(self, bg='white', width=LARGEUR, height=HAUTEUR)
        self.canvas.pack()

        # Variable.
        self.present_paths = []
        self.graph = graph
        self.should_stop = False
        self.should_show_routes = True

        self.min_x = min([lieu.x for lieu in self.graph.list_lieu])
        self.min_y =  min([lieu.y for lieu in self.graph.list_lieu])
        self.max_x =  max([lieu.x for lieu in self.graph.list_lieu])
        self.max_y =  max([lieu.y for lieu in self.graph.list_lieu])


        # Crée les boutons.
        self.button_matrix = tk.Button(text="Matrix OD", command=self.display_matrix)
        self.button_best_routes = tk.Button(text="Display Best routes", command=self.show_best_routes)
        self.button_matrix.pack(side=tk.BOTTOM)
        self.button_best_routes.pack(side=tk.BOTTOM)

        # Texte - Information
        self.infoText = tk.StringVar()
        self.text1 = tk.Label(self, textvariable=self.infoText)
        self.text1.pack(side=tk.BOTTOM)

        # Crée les villes.
        self.create_nodes()

        # Gère les évènements à la pression de certaines touches.
        self.bind("<Escape>", self.stop)
    

    # Affiche les différentes informations de meilleurs coups
    def draw_information(self, nb_iteration, best_path, best_distance) -> None:
        self.infoText.set("Meilleur distance: "+ str(best_path)+"\nMeilleur chemin: "+str(round(best_distance, 2))+"\tNombre itérations: "+str(nb_iteration))

    # Affiche la route principale.
    def draw_path(self, node1, node2) -> None:
        self.present_paths.append(self.canvas.create_line(self.rescale_x(node1.x), self.rescale_y(node1.y), self.rescale_x(node2.x), self.rescale_y(node2.y), arrow=tk.LAST, width=2, dash=(10, ), fill='#00f'))

    # Affiche les routes secondaires.
    def draw_path_color(self, node1, node2) -> None:
        self.present_paths.append(self.canvas.create_line(self.rescale_x(node1.x), self.rescale_y(node1.y), self.rescale_x(node2.x), self.rescale_y(node2.y), arrow=tk.LAST, fill='#aaa', width=1))

    # Reset la variable chemin.
    def reset_paths(self) -> None:
        for i in range(len(self.present_paths)):
            self.canvas.delete(self.present_paths[i])

        self.present_paths = []

    # Affiche les villes sous forme d'ellipse.
    def create_nodes(self) -> None:
        for lieu in self.graph.list_lieu:
            x, y = self.rescale_x(lieu.x), self.rescale_y(lieu.y)

            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="#00f")

    # Ouvre une nouvelle fenêtre pour afficher la matrice Origine - Destination.
    def display_matrix(self) -> None:

        new = tk.Toplevel(self)
        new.title("Matrix OD")

        frame = tk.Frame(new)

        for i in range(self.graph.nb_lieu):
            for j in range(self.graph.nb_lieu):
                text = round(self.graph.matrice_od[i, j], 2)
                if i == j:
                    tk.Label(frame, text=text, fg='#f00').grid(row=i, column=j)
                else:
                    tk.Label(frame, text=text).grid(row=i, column=j)

        frame.pack(expand=True)

    # Met une variable à True pour arrêter le programme.
    def stop(self, event) -> None:
        self.should_stop = True

    # Inverse la valeur de la variable (Vrai devient Faux et Faux devient Vrai). Utilisé lors de l'affichage des routes secondaires.
    def show_best_routes(self) -> None:
        self.should_show_routes = not(self.should_show_routes)
    
    def rescale_x(self, x) -> float:
        return ((LARGEUR - 10 - 10) * (x - self.min_x)) / (self.max_x - self.min_x) + 10
    
    def rescale_y(self, y) -> float:
        return ((HAUTEUR - 10 - 10) * (y - self.min_y)) / (self.max_y - self.min_y) + 10