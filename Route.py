class Route:

    def __init__(self):
        self.ordre = []

    def __getitem__(self, index):
        return self.ordre[index]
    
    def __set__(self, value):
        self.ordre.append(value)

    def __repr__(self) -> str:
        return 'Ordre: '+', '.join(self.ordre)
    
    def __len__(self):
        return len(self.ordre)