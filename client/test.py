from time import sleep
from machine import Pin
import modules.secrets as secrets
from modules.store import Store
from modules.display import Display
from modules.network import Network
from modules.rotary import Rotary

SSID=secrets.SSID
PWD=secrets.PWD
MQTT_HOST=secrets.MQTT_HOST
MQTT_USERNAME=secrets.MQTT_USERNAME
MQTT_PASSWORD=secrets.MQTT_PASSWORD
MQTT_PUBLISH_TOPIC=secrets.MQTT_PUBLISH_TOPIC
MQTT_CLIENT_ID=secrets.MQTT_CLIENT_ID

led = Pin(4, Pin.OUT)
button = Pin(5, Pin.IN, Pin.PULL_UP)

store = Store()
display = Display()
network = Network(SSID, PWD, MQTT_CLIENT_ID, MQTT_HOST, MQTT_USERNAME, MQTT_PASSWORD)

display.splash_screen()
sleep(2) #Splash Screen Delay

display.boot_screen("Booting...","Connecting to WiFi","")

try:
    ip = network.wifi_connect()
except:
    print('Trouble connecting to WiFi')
display.boot_screen("Booting...","Connecting to server", ip)


try:
    network.mqtt_connect()
except ValueError:
    print('MQTT issues')
    
    
display.home_screen(0, "")

rotary = Rotary(0,1)
val = 0

def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        val = val + 1
        network.mqtt_send(MQTT_PUBLISH_TOPIC, store.get_values())
    elif change == Rotary.ROT_CCW:
        if val > 0:
            val = val - 1
            network.mqtt_send(MQTT_PUBLISH_TOPIC, store.get_values())
    display.home_screen(val, "")
        
rotary.add_handler(rotary_changed)

def get_button():
    return not button.value()

def button_press_function():
    led.on()
    print('LED ON')

def button_released_function():
    led.off()
    print('LED OFF')
    

# while True:
#     if get_button() == 1:
#         button_press_function()
#     else:
#         button_released_function()
#     sleep(2)
