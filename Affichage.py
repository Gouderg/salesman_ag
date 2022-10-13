from constante import *
from Graph import *
import tkinter as tk


class Affichage(tk.Tk):

    def __init__(self, graph):
        tk.Tk.__init__(self)

        # Create the canvas.
        self.title("Salesman Gen")
        self.canvas = tk.Canvas(self, bg='white', width=LARGEUR, height=HAUTEUR)
        self.canvas.pack()

        # Variable.
        self.present_paths = []
        self.graph = graph
        self.should_stop = False
        self.should_show_routes = True

        # Create Buttons
        self.button_matrix = tk.Button(text="Matrix OD", command=self.display_matrix)
        self.button_best_routes = tk.Button(text="Display Best routes", command=self.show_best_routes)
        self.button_matrix.pack(side=tk.BOTTOM)
        self.button_best_routes.pack(side=tk.BOTTOM)


        self.infoText = tk.StringVar()
        self.text1 = tk.Label(self, textvariable=self.infoText)
        self.text1.pack(side=tk.BOTTOM)

        # Create points.
        self.create_nodes()

        # Bind keys.
        self.bind("<Escape>", self.stop)
    
    def draw_information(self, nb_iteration, best_path, best_distance):
        self.infoText.set("Nombre itérations: " + str(nb_iteration)+", Meilleur distance: "+ str(best_path)+"\nMeilleur chemin: "+ str(best_distance))

    def draw_path(self, node1, node2):
        self.present_paths.append(self.canvas.create_line(node1.x, node1.y, node2.x, node2.y, arrow=tk.LAST, width=1))

    def draw_path_color(self, node1, node2):
        self.present_paths.append(self.canvas.create_line(node1.x, node1.y, node2.x, node2.y, arrow=tk.LAST, fill='red', width=1, offset=20))

    def reset_paths(self):
        for i in range(len(self.present_paths)):
            self.canvas.delete(self.present_paths[i])

        self.present_paths = []

    def create_nodes(self):
        for lieu in self.graph.list_lieu:
            x, y = lieu.x, lieu.y

            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="#00f")

    def display_matrix(self):

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

    def stop(self, event):
        self.should_stop = True

    def show_best_routes(self):
        self.should_show_routes = not(self.should_show_routes)
  
