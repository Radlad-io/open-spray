from machine import Pin, PWM
import utime as time
import micropython

print('test')

class Infrared:
   def __init__(self, pin):
       self.led_pin = Pin(pin, Pin.IN, Pin.PULL_DOWN)

       
       

        
       
#    def rotary_change(self, pin):
#       new_status = (self.dt_pin.value() <<1) | self.clk_pin.value()
#       if new_status == self.last_status:
#          return
#       transition = (self.last_status <<2) | new_status
#       # Schedules calling the handlers
#       if transition  == 0b1110:
#          micropython.schedule(self.call_handlers, Rotary.ROT_CW)
#       elif transition == 0b1101:
#          micropython.schedule(self.call_handlers, Rotary.ROT_CCW)
#       self.last_status = new_status
