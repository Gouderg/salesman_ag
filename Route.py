class Route:

    def __init__(self, ordre = []) -> None:
        self.ordre = ordre

    # Permet de gérer les objets comme une liste (Autorise les opérations de slicing).
    def __getitem__(self, index) -> int:
        return self.ordre[index]
    
    # Permet de gérer les assignements sur l'objet.
    def __setitem__(self, index, value) -> None:
        self.ordre[index] = value

    # Donne une représentation de l'objet quand on l'affiche.
    def __repr__(self) -> str:
        a = [str(elt) for elt in self.ordre]
        return '"Ordre: '+', '.join(a) + ", "+ str(a[0])+ '"'
    
    # Renvoie la taille de la liste quand on demande la taille de l'objet.
    def __len__(self) -> int:
        return len(self.ordre)
    
    # Pousse une valeur à la fin de la liste.
    def addValue(self, value) -> None:
        self.ordre.append(value)

    # Permet de réaliser des comparaisons.
    def __lt__(self, other):
        if isinstance(other, Route):
            return True # Aled -> Implémenter mais pas utilisé car ranger selon fitness.
        else:
            return NotImplemented
    
