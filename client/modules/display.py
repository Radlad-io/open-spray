# Modules.Display
from picographics import PicoGraphics, DISPLAY_ROUND_LCD_240X240, PEN_RGB565
import jpegdec
import modules.store as Store

store = Store.Store()

def remap(x, in_min, in_max, out_min, out_max):
    """ Maps two ranges together """
    return int((x-in_min) * (out_max-out_min) / (in_max - in_min) + out_min)

display = PicoGraphics(display=DISPLAY_ROUND_LCD_240X240, pen_type=PEN_RGB565, rotate=180)
WIDTH, HEIGHT = display.get_bounds()

arrows = jpegdec.JPEG(display)
arrows.open_file("assets/arrows.jpg")
arrow = jpegdec.JPEG(display)
arrow.open_file("assets/arrow.jpg")

class Display:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Display, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.WIDTH, HEIGHT = display.get_bounds()
        self.WHITE = display.create_pen(255, 255, 255)
        self.BLACK = display.create_pen(0, 0, 0)
        self.GRAY = display.create_pen(85, 85, 85)
        self.TEXT_COLOR = display.create_pen(255, 255, 255)
        self.BACKGROUND_COLOR = display.create_pen(228, 169, 70)
        self.RED_COLOR = display.create_pen(255, 0, 0)
        self.GREEN_COLOR = display.create_pen(0, 255, 0)
        self.BLUE_COLOR = display.create_pen(0, 0, 255)
        self.ACITVE_COLOR = [225,95,115]
        self.clear()
        
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
        index = store.get_MENU_INDEX()
        if index == 0:
            self.background_comp()
            self.color_screen()
        
        if index == 1:
            self.background_comp()
            self.params_screen()
        
        if index == 2:
            self.background_comp()
            self.spray_screen()
        
        self.menu_position_indicator(index)

    def background_comp(self):
        display.set_pen(self.BLACK)
        display.clear()
        self.ACITVE_COLOR = [store.get_R(),store.get_G(),store.get_B()]
        color = display.create_pen(self.ACITVE_COLOR[0], self.ACITVE_COLOR[1],self.ACITVE_COLOR[2])
        display.set_pen(color)
        display.circle(120, 120, 125)
        display.set_pen(self.BLACK)
        display.circle(120, 120, 108)

    def color_screen(self):
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
        rValue = remap(store.get_R(), 0, 255, 0, 100)
        gValue = remap(store.get_G(), 0, 255, 0, 100)
        bValue = remap(store.get_B(), 0, 255, 0, 100)
        display.rectangle(105, 95, rValue, 10)
        display.set_pen(self.GREEN_COLOR)
        display.rectangle(105, 120, gValue, 10)
        display.set_pen(self.BLUE_COLOR)
        display.rectangle(105, 145, bValue, 10)
    
    def params_screen(self):
        # TEXT
        display.set_pen(self.WHITE)
        display.text("PARAMS", 50, 50, 200, 4)
        display.text("ALPHA", 35, 95, 200, 2)
        display.text("SIZE", 35, 120, 200, 2)
        display.text("SPREAD", 35, 145, 200, 2)
        # PROGRESS BARS
        display.set_pen(self.GRAY)
        display.rectangle(105, 97, 100, 10)
        display.rectangle(90, 122, 115, 10)
        display.rectangle(115, 147, 90, 10)
        display.set_pen(self.WHITE)
        aValue = remap(store.get_A(), 0, 1, 0, 100)
        siValue = remap(store.get_size(), 0, 1, 0, 115)
        spValue = remap(store.get_spread(), 0, 1, 0, 90)
        display.rectangle(105, 97, aValue, 10)
        display.rectangle(90, 122, siValue, 10)
        display.rectangle(115, 147, spValue, 10)
        
    def spray_screen(self):
        # TEXT

        display.set_pen(self.WHITE)
        display.text("LAYERS", 60, 50, 200, 4)
        # PROGRESS BARS
        arrows.decode(40, 100, jpegdec.JPEG_SCALE_FULL, dither=True)
        display.set_pen(self.RED_COLOR)
        display.circle(74, 130, 18)
        display.set_pen(self.BLACK)
        display.circle(74, 130, 14)
        display.set_pen(self.WHITE)
        display.text("{:02d}".format(store.SPRAY_INDEX), 66, 123, 200, 2)
        display.text("SPRAY", 48, 156, 200, 2)
        
        arrow.decode(135, 100, jpegdec.JPEG_SCALE_FULL, dither=True)
        display.set_pen(self.BLUE_COLOR)
        display.circle(169, 130, 18)
        display.set_pen(self.BLACK)
        display.circle(169, 130, 14)
        display.set_pen(self.WHITE)
        display.text("BACK", 148, 156, 200, 2)
        
                    

    def menu_position_indicator(self, position):
        # MENU INDICATOR
        display.set_pen(self.WHITE)
        display.circle(100, 200, 5)
        display.circle(120, 200, 5)
        display.circle(140, 200, 5)
        display.set_pen(self.BLACK)
        if position == 0:
            display.circle(100, 200, 4)
        elif position == 1:
            display.circle(120, 200, 4)
        elif position == 2:
            display.circle(140, 200, 4)
        display.update()
    
    def clear(self):
        display.clear()
        display.update()
    
    def update(self):
        display.update()

# test_display = Display()
# test_display.home_screen()
