import machine
import utime as time
from machine import Pin

dt = 1
clk = 2
dtPin = Pin(dt, Pin.IN, Pin.PULL_UP)
clkPin = Pin(clk, Pin.IN, Pin.PULL_UP)

def rotaryChange(pin):
    print(dtPin.value(), clk.Pin.value())

dtPin.irq(handler=rotaryChange, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
clkPin.irq(handler=rotaryChange, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
print(dtPin.value(), clkPin.value())

while True:
    time.sleep(0.1)