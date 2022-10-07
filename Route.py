class Route:

    def __init__(self):
        self.ordre = []
        self.fitness = 0

    def __getitem__(self, index):
        return self.ordre[index]

    def __repr__(self) -> str:
        a = [str(i) for i in self.ordre]
        return 'Ordre: '+', '.join(a)
    
    def __len__(self):
        return len(self.ordre)
    
    def addValue(self, value):
        self.ordre.append(value)
