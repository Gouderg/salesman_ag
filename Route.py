class Route:

    def __init__(self, ordre = []) -> None:
        self.ordre = ordre
        self.distance = 0

    def __getitem__(self, index) -> int:
        return self.ordre[index]
    
    def __setitem__(self, index, value) -> None:
        self.ordre[index] = value

    def __repr__(self) -> str:
        a = [str(elt) for elt in self.ordre]
        return '"Ordre: '+', '.join(a) + ", "+ str(a[0])+ '"'
    
    def __len__(self) -> int:
        return len(self.ordre)
    
    def addValue(self, value) -> None:
        self.ordre.append(value)

    def __lt__(self, other):
        if isinstance(other, Route):
            return self.distance < other.distance
        else:
            return NotImplemented
    
    # def __gt__(self, other):
    #     if isinstance(other, Route):
    #         return self.distance > other.distance
    #     else:
    #         return NotImplemented
    
    # def __eq__(self, other):
    #     if isinstance(other, Route):
    #         a = [str(i) for i in self.ordre]
    #         b = [str(i) for i in other.ordre]

    #         return self.distance == other.distance and ''.join(a) == ''.join(b)
    #     else:
    #         return NotImplemented
    
