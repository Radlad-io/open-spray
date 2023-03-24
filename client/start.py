from time import sleep
from machine import Pin
import modules.secrets as secrets
from modules.display import Display
from modules.network import Network
from modules.rotary import Rotary

SSID=secrets.SSID
PWD=secrets.PWD
ENDPOINT=secrets.ENDPOINT
PORT = secrets.PORT
led = Pin(4, Pin.OUT)
button = Pin(5, Pin.IN, Pin.PULL_UP)

display = Display()
network = Network(SSID, PWD)

display.splash_screen()

sleep(2) #Splash Screen Delay
display.boot_screen("Booting...","Connecting to WiFi","")

try:
    ip = network.connect()
except:
    print('Trouble connecting to WiFi')
display.boot_screen("Booting...","Establishing WebSockets", ip)


try:
    network.http_request()
except ValueError:
    print('WebSocket issues')
    
    
display.home_screen(0, ip)

rotary = Rotary(0,1)
val = 0

def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        val = val + 1
    elif change == Rotary.ROT_CCW:
        if val > 0:
            val = val - 1
    display.home_screen(val, ip)
        
rotary.add_handler(rotary_changed)

def get_button():
    return not button.value()

def button_press_function():
    led.value(1)
    print('LED ON')

def button_released_function():
    led.value(0)
    print('LED OFF')
    
while True:
    if get_button() == 1:
        button_press_function()
    else:
        button_released_function()
    led.value(0)
    sleep(0.5)
