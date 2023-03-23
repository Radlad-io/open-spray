# Modules.Display

from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_RGB565

class Display:
    
    def __init__(self):
        self.TEST = "test"
        self.display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_RGB565, rotate=90)
        self.WIDTH, HEIGHT = self.display.get_bounds()
        self.WHITE = self.display.create_pen(255, 255, 255)
        self.BLACK = self.display.create_pen(0, 0, 0)
        
    def splash_screen(self):
        self.display.set_pen(self.BLACK)
        self.display.clear()
        self.display.set_pen(self.WHITE)
        self.display.text("Bit Spray", 12, 65, 200, 8)
        self.display.update()
        
    def boot_screen(self, heading, status, footer):
        self.display.set_pen(self.BLACK)
        self.display.clear()
        self.display.set_pen(self.WHITE)
        self.display.text("Bit Spray", 12, 10, 200, 8)
        self.display.text(heading, 12, 140, 200, 2)
        self.display.text(status, 12, 160, 200, 3)
        self.display.text(footer, 12, 215, 200, 2)
        self.display.update()
        
    def home_screen(self, spray_index, footer):
        self.display.set_pen(self.BLACK)
        self.display.clear() 
        self.display.set_pen(self.WHITE)
        self.display.text("Bit Spray", 12, 10, 200, 4)
        self.display.text("Spray selected", 12, 45, 200, 2)
        self.display.text(str(spray_index), 12, 65, 200, 6)
        self.display.text(footer, 12, 215, 200, 2)
        self.display.update()
    
    def clear(self):
        self.display.clear()