from machine import Pin, PWM

rLED_ONE = Pin(4, Pin.OUT)
gLED_ONE = Pin(5, Pin.OUT)
bLED_ONE = Pin(6, Pin.OUT)


rLED_TWO = Pin(10, Pin.OUT)
gLED_TWO = Pin(11, Pin.OUT)
bLED_TWO = Pin(12, Pin.OUT)


rLED_Three = Pin(21, Pin.OUT)
gLED_Three = Pin(22, Pin.OUT)
bLED_Three = Pin(26, Pin.OUT)


rLED_ONE.on()
gLED_ONE.on()
bLED_ONE.off()

rLED_TWO.on()
gLED_TWO.off()
bLED_TWO.on()

rLED_Three.off()
gLED_Three.on()
bLED_Three.on()
