from time import sleep
import network
import socket


class Network:
    
    def __init__(self, SSID, PWD):
       self.SSID = SSID
       self.PWD = PWD
       
    def connect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.SSID, self.PWD)
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            sleep(1)
        self.IP = wlan.ifconfig()[0]
        print(f'Connected to: {self.SSID}', '\n', f'{self.IP}')
        return self.IP