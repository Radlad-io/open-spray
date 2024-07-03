import modules.rotary as Rotary
import modules.display as Display
import modules.store as Store
import modules.sound as Sound
import modules.bluetooth as bluetooth

store = Store.Store()
display = Display.Display()
sound = Sound.Sound()

class Inputs:
    
    def __init__(self):
        self.ADJUSTMENT_FACTOR = 5;
        self.rotary_01 = Rotary.Rotary(1,2,3,4,5,6,True,False,False)
        self.rotary_02 = Rotary.Rotary(7,8,9,10,11,12,False,True,False)
        self.rotary_03 = Rotary.Rotary(13,14,15,21,22,26,False,False,True)
        self.rotary_01.add_handler(self.firstHandler)
        self.rotary_02.add_handler(self.secondHandler)
        self.rotary_03.add_handler(self.thirdHandler)
        self.sound_duration = 1/32
        
    def firstHandler(self, change):
#       Exit if not connected to BT
        if store.get_connected() == False:
            return
#       Sync state over BT required
        bluetooth.sync_required = True
        
#       Change state based on menu context
        if change == Rotary.Rotary.ROT_CW:
            if store.get_MENU_INDEX() == 0:
                if store.get_R() < 255:
                    store.set_R(store.get_R() + self.ADJUSTMENT_FACTOR)
            elif store.get_MENU_INDEX() == 1:
                if store.get_A() < 1.0:
                    store.set_A(store.get_A() + 0.05)
            elif store.get_MENU_INDEX() == 2:
                if store.get_spray_index() < store.get_spray_count():
                    store.set_spray_index(store.get_spray_index() + 1)
                else:
                    store.set_spray_index(0)

#       Change state based on menu context
        elif change == Rotary.Rotary.ROT_CCW:
            if store.get_MENU_INDEX() == 0:
                if store.get_R() > 0:
                    store.set_R(store.get_R() - self.ADJUSTMENT_FACTOR)
            elif store.get_MENU_INDEX() == 1:
                if store.get_A() > 0:
                    val = store.get_A() - 0.05
                    if val < 0:
                        val = 0
                    store.set_A(val)
            elif store.get_MENU_INDEX() == 2:
                if store.get_spray_index() > 0:
                    store.set_spray_index(store.get_spray_index() - 1)
                else:
                    store.set_spray_index(store.get_spray_count())
#       Change menu context
        elif change == Rotary.Rotary.SW_PRESS:
            store.set_MENU_INDEX(0)
            display.update()
#       elif change == Rotary.Rotary.SW_RELEASE:

        display.home_screen()


                
    def secondHandler(self, change):
#       Exit if not connected to BT
        if store.get_connected() == False:
            return
#       Sync state over BT required
        bluetooth.sync_required = True

#       Change state based on menu context
        if change == Rotary.Rotary.ROT_CW:
            if store.get_MENU_INDEX() == 0:
                if store.get_G() < 255:
                    store.set_G(store.get_G() + self.ADJUSTMENT_FACTOR)
            elif store.get_MENU_INDEX() == 1:
                if store.get_size() < 1.0:
                    store.set_size(store.get_size() + 0.05)
            elif store.get_MENU_INDEX() == 2:
                return

#       Change state based on menu context
        elif change == Rotary.Rotary.ROT_CCW:
            if store.get_MENU_INDEX() == 0:
                if store.get_G() > 0:
                    store.set_G(store.get_G() - self.ADJUSTMENT_FACTOR)
            elif store.get_MENU_INDEX() == 1:
                if store.get_size() > 0:
                    val = store.get_size() - 0.05
                    if val < 0:
                        val = 0
                    store.set_size(val)
            elif store.get_MENU_INDEX() == 2:
                return
#       Change state based on menu context
        elif change == Rotary.Rotary.SW_PRESS:
            store.set_MENU_INDEX(1)
            display.update()
        display.home_screen()

    def thirdHandler(self, change):
#       Exit if not connected to BT
        if store.get_connected() == False:
            return
#       Sync state over BT required
        bluetooth.sync_required = True
        
#       Change state based on menu context
        if change == Rotary.Rotary.ROT_CW:
            if store.get_MENU_INDEX() == 0:
                if store.get_B() < 255:
                    store.set_B(store.get_B() + self.ADJUSTMENT_FACTOR)
            elif store.get_MENU_INDEX() == 1:
                if store.get_spread() < 1.0:
                    store.set_spread(store.get_spread() + 0.05)
            elif store.get_MENU_INDEX() == 2:
                return 
                    
#       Change state based on menu context
        elif change == Rotary.Rotary.ROT_CCW:
            if store.get_MENU_INDEX() == 0:
                if store.get_B() > 0:
                    store.set_B(store.get_B() - self.ADJUSTMENT_FACTOR)
            elif store.get_MENU_INDEX() == 1:
                if store.get_spread() > 0:
                    val = store.get_spread() - 0.05
                    if val < 0:
                        val = 0
                    store.set_spread(val)
            elif store.get_MENU_INDEX() == 2:
                store.set_undo(True)
            
#       Change state based on menu context          
        elif change == Rotary.Rotary.SW_PRESS:
            store.set_MENU_INDEX(2)
            display.update()

        display.home_screen()



