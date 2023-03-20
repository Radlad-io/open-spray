from time import sleep
import network
import socket
from time import sleep
import machine
import micropython
from display import Display
# from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_RGB565

# display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_RGB565, rotate=90)

# WIDTH, HEIGHT = Display.get_bounds()
# WHITE = display.create_pen(255, 255, 255)
# BLACK = display.create_pen(0, 0, 0)
# HEADING = "booting..."
# DESCRIPTION="Connecting to network"

SSID="Eattherich"
PWD="superSecure"

def connect():
    global DESCRIPTION
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PWD)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected to: {SSID}', '\n', f'{ip}')
    Display.clear()
    DESCRIPTION = 'Connected.'
    Display.update_display()


# def update_display():
#     display.set_pen(BLACK)  # Set pen
#     display.clear()         # Fill the screen with the colour
#     display.set_pen(WHITE)    # Set pen to black
#     display.text("Open Spray", 12, 10, 200, 8)  # Add some text
#     display.text(HEADING, 12, 140, 200, 2)  # and a bit more tiny text
#     display.text(DESCRIPTION, 12, 160, 200, 3)  # and some more text
#     display.update()          # Update the display
    

Display.update_display()
try:
    connect()
except KeyboardInterrupt:
    print(f'Error connecting to {SSID}')
    machine.reset()
