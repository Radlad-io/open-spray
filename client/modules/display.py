# Modules.Display

from picographics import PicoGraphics, DISPLAY_ROUND_LCD_240X240, PEN_RGB565

def remap(x, in_min, in_max, out_min, out_max):
    """ Maps two ranges together """
    return int((x-in_min) * (out_max-out_min) / (in_max - in_min) + out_min)

display = PicoGraphics(display=DISPLAY_ROUND_LCD_240X240, pen_type=PEN_RGB565)

class Display:
    def __init__(self):
        self.WIDTH, HEIGHT = display.get_bounds()
        self.WHITE = display.create_pen(255, 255, 255)
        self.BLACK = display.create_pen(0, 0, 0)
        self.GRAY = display.create_pen(50, 50, 50)
        self.TEXT_COLOR = display.create_pen(255, 255, 255)
        self.BACKGROUND_COLOR = display.create_pen(228, 169, 70)
        self.RED_COLOR = display.create_pen(255, 0, 0)
        self.GREEN_COLOR = display.create_pen(0, 255, 0)
        self.BLUE_COLOR = display.create_pen(0, 0, 255)
        self.ACITVE_COLOR = [225,95,115]
        
    def splash_screen(self):
        display.set_pen(self.BLACK)
        display.clear()
        display.set_pen(self.WHITE)
        display.text("Bit Spray", 30, 60, 200, 7)
        display.text("www.BitSpray.art", 30, 165, 200, 2)
        display.update()
        
    def boot_screen(self, heading, status, footer):
        display.set_pen(self.BLACK)
        display.clear()
        display.set_pen(self.WHITE)
        display.text(heading, 28, 80, 200, 2)
        display.text(status, 28, 105, 200, 3)
        display.text(footer, 30, 155, 200, 2)
        display.update()
    
    def menu_screen(self):
        display.set_pen(self.BLACK)
        display.clear() 
        display.set_pen(self.WHITE)
        display.rectangle(50, 95, 140, 50)
        display.circle(50, 120, 24)
        display.circle(190, 119, 24)
        display.triangle(135, 35, 105, 35, 120, 20)
        display.triangle(135, 200, 105, 200, 120, 220)
        display.set_pen(self.BLACK)
        display.text("colors", 60, 105, 200, 4)
        display.set_pen(self.GRAY)
        display.text("sizes", 75, 160, 200, 4)
        display.set_pen(self.GRAY)
        display.text("layers", 60, 50, 200, 4)
        display.update()

    def home_screen(self):
        # BACKGOUND
        self.background_comp()
        self.progress_bars()
        self.menu_position_indicator(1)

    def background_comp(self):
        display.set_pen(self.BLACK)
        display.clear()
        color = display.create_pen(self.ACITVE_COLOR[0], self.ACITVE_COLOR[1],self.ACITVE_COLOR[2])
        display.set_pen(color)
        display.circle(120, 120, 125)
        display.set_pen(self.BLACK)
        display.circle(120, 120, 108)

    def progress_bars(self):
        # TEXT
        display.set_pen(self.WHITE)
        display.text("COLOR", 65, 50, 200, 4)
        display.text("red", 35, 95, 200, 2)
        display.text("green", 35, 120, 200, 2)
        display.text("blue", 35, 145, 200, 2)
        # PROGRESS BARS
        display.rectangle(105, 95, 100, 10)
        display.rectangle(105, 120, 100, 10)
        display.rectangle(105, 145, 100, 10)
        display.set_pen(self.RED_COLOR)
        rValue = remap(self.ACITVE_COLOR[0], 0, 255, 0, 100)
        gValue = remap(self.ACITVE_COLOR[1], 0, 255, 0, 100)
        bValue = remap(self.ACITVE_COLOR[2], 0, 255, 0, 100)
        display.rectangle(105, 95, rValue, 10)
        display.set_pen(self.BLUE_COLOR)
        display.rectangle(105, 120, gValue, 10)
        display.set_pen(self.GREEN_COLOR)
        display.rectangle(105, 145, bValue, 10)

    def menu_position_indicator(self, position):
        # MENU INDICATOR
        display.set_pen(self.WHITE)
        display.circle(100, 200, 5)
        display.circle(120, 200, 5)
        display.circle(140, 200, 5)
        display.set_pen(self.BLACK)
        if position == 1:
            display.circle(100, 200, 4)
        elif position == 2:
            display.circle(120, 200, 4)
        elif position == 3:
            display.circle(140, 200, 4)
        display.update()
    
    def clear(self):
        self.display.clear()
        
# FOR TESTING
# lcd_display = Display()
# lcd_display.splash_screen()