class Route:

    def __init__(self):
        self.ordre = []
        self.fitness = 0

    def __getitem__(self, index):
        return self.ordre[index]

    def __repr__(self) -> str:
        return 'Ordre: '+', '.join(self.ordre)
    
    def __len__(self):
        return len(self.ordre)
    
    def addValue(self, value):
        self.ordre.append(value)
