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

led = Pin(27, Pin.OUT)
button = Pin(28, Pin.IN, Pin.PULL_UP)

store = Store()
display = Display()
network = Network(SSID, PWD, MQTT_CLIENT_ID, MQTT_HOST, MQTT_USERNAME, MQTT_PASSWORD)

display.splash_screen()
sleep(4) #Splash Screen Delay

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
    
    
sleep(2)
display.home_screen()

val = 0
def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        val = val + 1
        print(val)
#         network.mqtt_send(MQTT_PUBLISH_TOPIC, store.get_values())
    elif change == Rotary.ROT_CCW:
        if val > 0:
            val = val - 1
#             network.mqtt_send(MQTT_PUBLISH_TOPIC, store.get_values())
            print(val)
    display.home_screen()
        

# rotary_01 = Rotary(13,14,15,21,22,26,0,65535,65535)
# rotary_02 = Rotary(7,8,9,10,11,12,65535,0,65535)
rotary_03 = Rotary(1,2,3,4,5,6,0,0,0)

# rotary_01.add_handler(rotary_changed)
# rotary_02.add_handler(rotary_changed)

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
