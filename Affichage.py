from constante import LARGEUR, HAUTEUR, NB_LIEUX

import tkinter as tk

# https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
class Affichage(tk.Tk):

    def __init__(self, list_lieux):
        tk.Tk.__init__(self)

        self.title("Salesman Gen")
        self.canvas = tk.Canvas(self, bg='white', width=LARGEUR, height=HAUTEUR)
        self.canvas.pack()


        self.infoText = tk.StringVar()

        self.text1 = tk.Label(self, textvariable=self.infoText)
        self.text1.pack()

        # Create points.
        self.create_nodes(list_lieux)

        # Bind keys.
        self.bind("<Escape>", self.stop)
    
    def draw(self, nb_iteration, best_path):
        self.infoText.set("Nombre itérations: " +str(nb_iteration)+", Meilleur chemin: "+' - '.join(best_path))

    def draw_path(self,node1,node2):
        self.canvas.create_line(node1.x, node1.y, node2.x, node2.y, arrow=tk.LAST)



    
    def create_nodes(self, list_lieux):
        #self.canvas.create_oval(0, 0, 15, 15)
        #self.canvas.create_oval(LARGEUR-15, HAUTEUR-15, LARGEUR, HAUTEUR)



        for lieu in list_lieux:
            x, y = lieu.x, lieu.y

            self.canvas.create_oval(x-15, y-15, x+15, y+15)
        

    def stop(self, event):
        # self.withdraw()
        self.destroy()
