from time import sleep
from machine import Pin
import uasyncio as asyncio

from modules.store import Store
from modules.display import Display
from modules.network import Network
from modules.rotary import Rotary
from modules.inputs import Inputs
from modules.sound import Sound
import modules.bluetooth as bluetooth

inputs = Inputs()
led = Pin(27, Pin.OUT)
button = Pin(28, Pin.IN, Pin.PULL_UP)

store = Store()
display = Display()
display.clear()

sound = Sound()
sound.muted = True

display.splash_screen()
sound.play_intro()
sleep(2) #Splash Screen Delay

display.boot_screen("No connection:", "Please reconnect", "using bluetooth")
asyncio.run(bluetooth.init())


