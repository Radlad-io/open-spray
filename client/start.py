from time import sleep
import modules.secrets as secrets
from modules.display import Display
from modules.network import Network
from modules.rotary import Rotary

SSID=secrets.SSID
PWD=secrets.PWD
ENDPOINT=secrets.ENDPOINT
API_ROUTE=secrets.API_ROUTE

display = Display()
network = Network(SSID, PWD)

display.splash_screen()

sleep(2) #Splash Screen Delay
display.boot_screen("Booting...","Connecting to WiFi","")

ip = network.connect()
display.boot_screen("Booting...","Establishing WebSockets", ip)

sleep(2)
display.home_screen(0)

rotary = Rotary(0,1)
val = 0

def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        val = val + 1
    elif change == Rotary.ROT_CCW:
        val = val - 1
    display.home_screen(val)
        
rotary.add_handler(rotary_changed)