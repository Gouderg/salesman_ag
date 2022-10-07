class Route:

    def __init__(self):
        self.ordre = []
        self.distance = 0

    def __getitem__(self, index):
        return self.ordre[index]

    def __repr__(self) -> str:
        a = [str(elt) for elt in self.ordre]
        return '"Ordre: '+', '.join(a) + '"'
    
    def __len__(self):
        return len(self.ordre)
    
    def __lt__(self, other):
        if isinstance(other, Route):
            return self.distance < other.distance
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Route):
            return self.distance > other.distance
        else:
            return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Route):
            return self.distance == other.distance
        else:
            return NotImplemented
    
    def addValue(self, value):
        self.ordre.append(value)
