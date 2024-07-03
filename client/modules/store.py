
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
        self.A = 0.5
        self.SIZE = 0.5
        self.SPREAD = 0.5
        self.SPRAY_INDEX = 1
        self.SPRAY_COUNT = 12
        self.LAYER_INDEX = 0
        self.UNDO = False
        self.MENU_INDEX = 0
        self.CONNECTED = False;
        
    def get_connected(self):
        return self.CONNECTED
    
    def set_connected(self, value):
        self.CONNECTED = value
        
    def get_values_as_json(self):
        values = f'{{"rgba": "[{self.R},{self.G},{self.B},{self.A}]","size": "{self.SIZE}","spread": "{self.SPREAD}", "sprayIndex": "{self.SPRAY_INDEX}", "layerIndex": "{self.LAYER_INDEX}", "undo": "{self.UNDO}"}}'
        return values
    
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
        
    def get_A(self):
        return self.A
    
    def set_A(self, value):
        self.A = value
    
    def get_size(self):
        return self.SIZE
    
    def set_size(self, value):
        self.SIZE = value
    
    def get_spread(self):
        return self.SPREAD
    
    def set_spread(self, value):
        self.SPREAD = value
        
    def get_spray_index(self):
        return self.SPRAY_INDEX
        
    def set_spray_index(self, value):
        self.SPRAY_INDEX = value
        
    def get_spray_count(self):
        return self.SPRAY_COUNT
        
    def set_spray_count(self, value):
        self.SPRAY_COUNT = value
        
    def get_undo(self):
        return self.UNDO
        
    def set_undo(self, value):
        self.UNDO = value
        
    def get_MENU_INDEX(self):
        return self.MENU_INDEX
        
    def set_MENU_INDEX(self, value):
        self.MENU_INDEX = value

        
  



