from machine import Pin
import utime as time
import micropython
from modules.ubutton import uButton

class Rotary:

   ROT_CW = 1   # Abstract Pin.IRQ_FALLING
   ROT_CCW = 2   # Abstract Pin.IRQ_FALLING
   SW_PRESS = 4   # Abstract Pin.IRQ_FALLING
   SW_RELEASE = 8   # Abstract Pin.IRQ_RISING

   def __init__(self, dt, clk, sw, r_pin, g_pin, b_pin, r_value, g_value, b_value):
      # Defines dt & clk pins
      self.dt_pin = Pin(dt, Pin.IN, Pin.PULL_UP)
      self.clk_pin = Pin(clk, Pin.IN, Pin.PULL_UP)
      self.sw_pin = Pin(sw, Pin.IN, Pin.PULL_DOWN)
      # 2bit Binary Number that stores last value for encoder
      self.last_status = (self.dt_pin.value() <<1) | self.clk_pin.value()
      # Pin Change Events
      self.dt_pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
      self.clk_pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
      self.sw_pin.irq(handler=self.switch_detect, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
      # Callbacks
      self.handlers = []
      self.last_button_status = self.sw_pin.value()
      self.rLED = Pin(r_pin, Pin.OUT, Pin.PULL_UP)
      self.gLED = Pin(g_pin, Pin.OUT, Pin.PULL_UP)
      self.bLED = Pin(b_pin, Pin.OUT, Pin.PULL_UP)
      
#     Rest all led Pins
      self.rLED.on()
      self.gLED.on()
      self.bLED.on()
      
      if r_value == True:
          self.rLED.off()
           
      if g_value == True:
          self.gLED.off()
          
      if b_value == True:
          self.bLED.off()

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
            micropython.schedule(self.call_handlers, Rotary.SW_PRESS)
        else:
            micropython.schedule(self.call_handlers, Rotary.SW_RELEASE)
        
   def add_handler(self, handler):
      self.handlers.append(handler)

   def call_handlers(self, type):
      for handler in self.handlers:
         handler(type)


