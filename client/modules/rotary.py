from machine import Pin
import utime as time
import micropython

class Rotary:

   ROT_CW = 1   # Abstract Pin.IN
   ROT_CCW = 2   # Abstract Pin.OUT
   SW_PRESS = 4   # Abstract Pin.IRQ_FALLING
   SW_RELEASE = 8   # Abstract Pin.IRQ_RISING

   def __init__(self, dt, clk):
      # Defines dt & clk pins
      self.dt_pin = Pin(dt, Pin.IN, Pin.PULL_DOWN)
      self.clk_pin = Pin(clk, Pin.IN, Pin.PULL_DOWN)
      # 2bit Binary Number that stores last value
      self.last_status = (self.dt_pin.value() <<1) | self.clk_pin.value()
      # Pin Change Events
      self.dt_pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
      self.clk_pin.irq(handler=self.rotary_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
      self.handlers = []

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

   def add_handler(self, handler):
      self.handlers.append(handler)

   def call_handlers(self, type):
      for handler in self.handlers:
         handler(type)

