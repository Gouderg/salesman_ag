class Route:

    def __init__(self):
        self.ordre = []

    def __get__(self, index):
        return self.ordre[index]
    
    def __set__(self, value):
        self.ordre.append(value)

    def __repr__(self) -> str:
        return ', '.join(self.ordre)