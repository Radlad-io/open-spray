from time import sleep
import network
import usocket

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
        IP = wlan.ifconfig()[0]
        print(f'Connected to: {self.SSID}', '\n', f'{IP}')
        return IP
    
    def http_request(self):
        s = usocket.socket()
        ai = usocket.getaddrinfo("192.168.50.252", 5000)
        print("Address infos:", ai)
        addr = ai[0][-1]
        print("Connect address:", addr)
        s.connect(addr)
        s.send(b"GET / HTTP/1.0\r\n\r\n")
        print(s.recv(4096))
        s.close()
    
            
