import tkinter as tk
from constante import LARGEUR, HAUTEUR
import time

# https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
class Affichage(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.canvas = tk.Canvas(self, bg='white', width=LARGEUR, height=HAUTEUR)
        self.canvas.pack()

        # Create points.
        self.create_nodes()

        # Bind keys.
        self.canvas.bind("<Escape>", self.stop)
    
    def update(self, i, j):
        self.canvas.create_rectangle(30, 70, i, j)

    
    def create_nodes(self):
        pass

    def stop(self):
        self.quit()

app = Affichage()

for i in range(1000):

    app.update(i, i)
    time.sleep(0.05)
    print(1)
