from machine import Pin, PWM
import utime as time
import micropython
import uasyncio
import random

class Rotary:

   ROT_CW = 1   # Abstract Pin.IRQ_FALLING
   ROT_CCW = 2   # Abstract Pin.IRQ_FALLING
   SW_PRESS = 4   # Abstract Pin.IRQ_FALLING
   SW_RELEASE = 8   # Abstract Pin.IRQ_RISING

   def __init__(self, dt, clk, sw, r_pin, g_pin, b_pin, r_value, g_value, b_value):
      # Defines dt & clk pins
      self.dt_pin = Pin(dt, Pin.IN, Pin.PULL_UP)
      self.clk_pin = Pin(clk, Pin.IN, Pin.PULL_UP)
      self.sw_pin = Pin(sw, Pin.IN, Pin.PULL_UP)
      # 2bit Binary Number that stores last value
      self.last_status = (self.dt_pin.value() <<1) | self.clk_pin.value()
      # Pin Change Events
      self.dt_pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
      self.clk_pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
      # Callbacks
      self.handlers = []
      self.last_button_status = self.sw_pin.value()
      self.PWM_FREQ  = 2000
      self.COLOUR_MAX = 65535
      self.rLED = PWM(Pin(r_pin, Pin.OUT))
      self.gLED = PWM(Pin(g_pin, Pin.OUT))
      self.bLED = PWM(Pin(b_pin, Pin.OUT))
      self.rLED.freq(2000)
      self.gLED.freq(2000)
      self.bLED.freq(2000)
      self.rLED.duty_u16(r_value)
      self.gLED.duty_u16(g_value)
      self.bLED.duty_u16(b_value)

   def rotary_change(self, pin):
      new_status = (self.dt_pin.value() <<1) | self.clk_pin.value()
      if new_status == self.last_status:
         return
      transition = (self.last_status <<2) | new_status
      # Schedules calling the handlers
      if transition  == 0b1110:
         micropython.schedule(self.call_handlers, Rotary.ROT_CW)
      elif transition == 0b1101:
         micropython.schedule(self.call_handlers, Rotary.ROT_CCW)
      self.last_status = new_status

   def switch_detect(self, pin):
        if self.last_button_status == self.sw_pin.value():
            return
        self.last_button_status = self.sw_pin.value()
        if self.sw_pin.value():
            print('Switch Released')
#             micropython.schedule(self.call_handlers, Rotary.SW_RELEASE)
        else:
            print('Switch Pressed')
#             micropython.schedule(self.call_handlers, Rotary.SW_PRESS)

   def add_handler(self, handler):
      self.handlers.append(handler)

   def call_handlers(self, type):
      for handler in self.handlers:
         handler(type)
         
   def rgb_led(self):
        print('cool')



# FOR TESTING

val = 0

def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        val = val + 1
        print(val)
    elif change == Rotary.ROT_CCW:
        if val > 0:
            val = val - 1
            print(val)
    elif change == Rotary.SW_PRESS:
        print('PRESS')
    elif change == Rotary.SW_RELEASE:
        print('RELEASE')

rotary_01 = Rotary(1,2,3,4,5,6,65535,65535,0)
# rotary_02 = Rotary(7,8,9,10,11,12,0,65535,65535)
# rotary_03 = Rotary(13,14,15,21,22,26,65535,0,65535)

#         
rotary_01.add_handler(rotary_changed)
# rotary_02.add_handler(rotary_changed)
# # rotary_03.add_handler(rotary_changed)


