from Graph import Graph
from constante import LARGEUR, HAUTEUR, NB_LIEUX

import tkinter as tk
import time
import random

# https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
class Affichage(tk.Tk):

    def __init__(self, list_lieux):
        tk.Tk.__init__(self)
        self.title("Salesman Gen")
        self.canvas = tk.Canvas(self, bg='white', width=LARGEUR, height=HAUTEUR)
        self.canvas.pack()

        # Create points.
        self.create_nodes(list_lieux)

        # Bind keys.
        self.bind("<Escape>", self.stop)
    
    def draw(self, i, j):
        pass

    
    def create_nodes(self, list_lieux):

        for key in list_lieux:
            x, y = list_lieux[key].x, list_lieux[key].y

            self.canvas.create_oval(x-15, y-15, x+15, y+15)
    
    def show_matrice(self):
        window = tk.Toplevel()
        

    def stop(self, event):
        # self.withdraw()
        self.destroy()


# Création du graph.
graph = Graph()
graph.charger_graph()
graph.charger_matrice_od()

# Création de l'affichage.
app = Affichage(graph.list_lieu)

# Boucle de mise en service.
for i in range(1000):

    app.update()
    app.update_idletasks()
    time.sleep(0.02)
