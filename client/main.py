from time import sleep
from machine import Pin
import modules.secrets as secrets
from modules.store import Store
from modules.display import Display
from modules.network import Network
from modules.rotary import Rotary
from modules.inputs import Inputs
from modules.sound import Sound


SSID=secrets.SSID
PWD=secrets.PWD
MQTT_HOST=secrets.MQTT_HOST
MQTT_USERNAME=secrets.MQTT_USERNAME
MQTT_PASSWORD=secrets.MQTT_PASSWORD
MQTT_PUBLISH_TOPIC=secrets.MQTT_PUBLISH_TOPIC
MQTT_CLIENT_ID=secrets.MQTT_CLIENT_ID


inputs = Inputs()
led = Pin(27, Pin.OUT)
button = Pin(28, Pin.IN, Pin.PULL_UP)

store = Store()
display = Display()
display.clear()

network = Network(SSID, PWD, MQTT_CLIENT_ID, MQTT_HOST, MQTT_USERNAME, MQTT_PASSWORD)
sound = Sound()

display.splash_screen()
sound.play_intro()
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
    
    
sleep(2)
display.home_screen()


def get_button():
    return not button.value()

def button_press_function():
    led.on()
    print('LED ON')

def button_released_function():
    led.off()
    print('LED OFF')
    

