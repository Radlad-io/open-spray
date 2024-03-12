
class Store:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Store, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.R = 100
        self.G = 175
        self.B = 75
        self.A = 1
        self.SIZE = 0.5
        self.SPRAY_INDEX = 0
        self.LAYER_INDEX = 0
        self.MENU_INDEX = 0
        
    def get_values_as_json(self):
        values = b'{"rgba": "[{self.R},{self.G},{self.B},{self.A}]", "sprayIndex": "{self.SPRAY_INDEX}", "layerIndex": "{self.LAYER_INDEX}"}'
        return values
    
    def get(self, value):
        return self[value]
    
    def get_R(self):
        return self.R
    
    def set_R(self, value):
        self.R = value
    
    def get_G(self):
        return self.G
    
    def set_G(self, value):
        self.G = value
        
    def get_B(self):
        return self.B
    
    def set_B(self, value):
        self.B = value
    
    def get_MENU_INDEX(self):
        return self.MENU_INDEX
        
    def set_MENU_INDEX(self, value):
        self.MENU_INDEX = value

        
  
