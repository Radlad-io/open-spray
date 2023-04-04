

class Store:
    
    def __init__(self):
        self.R = 0
        self.G = 0
        self.B = 0
        self.A = 0
        self.SIZE = 0.5
        self.SPRAY_INDEX = 0
        self.test()
        
    def get_values(self):
        values = {"r": f'{self.R}', "g": f'{self.G}', "b": f'{self.B}', "a": f'{self.A}', "size": f'{self.SIZE}', "sprayIndex": f'{self.SPRAY_INDEX}'}
        return values

    def test(self):
        print(self.get_values())
        
  