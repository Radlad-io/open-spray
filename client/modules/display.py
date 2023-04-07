# Modules.Display

from picographics import PicoGraphics, DISPLAY_ROUND_LCD_240X240, PEN_RGB565

class Display:
    
    def __init__(self):
        self.TEST = "test"
        self.display = PicoGraphics(display=DISPLAY_ROUND_LCD_240X240, pen_type=PEN_RGB565)
        self.WIDTH, HEIGHT = self.display.get_bounds()
        self.WHITE = self.display.create_pen(255, 255, 255)
        self.BLACK = self.display.create_pen(0, 0, 0)
        
    def splash_screen(self):
        self.display.set_pen(self.BLACK)
        self.display.clear()
        self.display.set_pen(self.WHITE)
        self.display.text("Bit Spray", 25, 75, 200, 6)
        self.display.update()
        
    def boot_screen(self, heading, status, footer):
        self.display.set_pen(self.BLACK)
        self.display.clear()
        self.display.set_pen(self.WHITE)
        self.display.text(heading, 28, 80, 200, 2)
        self.display.text(status, 28, 105, 200, 3)
        self.display.text(footer, 30, 155, 200, 2)
        self.display.update()
        
    def home_screen(self, spray_index, footer):
        self.display.set_pen(self.BLACK)
        self.display.clear() 
        self.display.set_pen(self.WHITE)
        self.display.text("Spray", 65, 55, 200, 4)
        self.display.text(str(spray_index), 95, 90, 200, 10)
        self.display.text(footer, 12, 75, 200, 4)
        self.display.update()
    
    def clear(self):
        self.display.clear()
        
# display = Display()
# 
# display.boot_screen("Booting...","Connecting to WiFi","192.99.91.20")
# 
# display.home_screen(8, "")