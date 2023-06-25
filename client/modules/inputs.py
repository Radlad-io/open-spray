import modules.rotary as Rotary
import modules.display as Display
import modules.store as Store
import modules.sound as Sound

store = Store.Store()
display = Display.Display()
sound = Sound.Sound()

class Inputs:
    
    def __init__(self):
        self.ADJUSTMENT_FACTOR = 5;
        self.rotary_01 = Rotary.Rotary(13,14,15,21,22,26,True,False,False)    
        self.rotary_02 = Rotary.Rotary(7,8,9,10,11,12,False,True,False)
        self.rotary_03 = Rotary.Rotary(1,2,3,4,5,6,False,False,True)
        self.rotary_01.add_handler(self.firstHandler)
        self.rotary_02.add_handler(self.secondHandler)
        self.rotary_03.add_handler(self.thirdHandler)
        self.sound_duration = 1/32
        
    def firstHandler(self, change):
        if change == Rotary.Rotary.ROT_CW:
            if store.get_R() < 255:
                store.set_R(store.get_R() + self.ADJUSTMENT_FACTOR)
    #         network.mqtt_send(MQTT_PUBLISH_TOPIC, store.get_values())
        elif change == Rotary.Rotary.ROT_CCW:
            if store.get_R() > 0:
                store.set_R(store.get_R() - self.ADJUSTMENT_FACTOR)
    #             network.mqtt_send(MQTT_PUBLISH_TOPIC, store.get_values())
        elif change == Rotary.Rotary.SW_PRESS:
            store.set_MENU_INDEX(0)
            display.update()
            print('first pressed')
        elif change == Rotary.Rotary.SW_RELEASE:
            print('first released')
        display.home_screen()
        
                
    def secondHandler(self, change):
        if change == Rotary.Rotary.ROT_CW:
            if store.get_G() < 255:
                store.set_G(store.get_G() + self.ADJUSTMENT_FACTOR)
        elif change == Rotary.Rotary.ROT_CCW:
            if store.get_G() > 0:
                store.set_G(store.get_G() - self.ADJUSTMENT_FACTOR)
        elif change == Rotary.Rotary.SW_PRESS:
            store.set_MENU_INDEX(1)
            display.update()
            print('second pressed')
        elif change == Rotary.Rotary.SW_RELEASE:
            print('second released')
        display.home_screen()

    def thirdHandler(self, change):
        if change == Rotary.Rotary.ROT_CW:
            if store.get_B() < 255:
                store.set_B(store.get_B() + self.ADJUSTMENT_FACTOR)
        elif change == Rotary.Rotary.ROT_CCW:
            if store.get_B() > 0:
                store.set_B(store.get_B() - self.ADJUSTMENT_FACTOR)
        elif change == Rotary.Rotary.SW_PRESS:
            store.set_MENU_INDEX(2)
            display.update()
            print('third pressed')
        elif change == Rotary.Rotary.SW_RELEASE:
            print('third released')
        display.home_screen()

