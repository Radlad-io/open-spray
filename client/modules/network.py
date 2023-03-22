from time import sleep
import network
import usocket as socket

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
    
    def open_socket(self, endpoint, port):
        try:
#             sockaddr = socket.getaddrinfo(endpoint, port)[0][-1]
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print(socket.error)
            
        s.connect((endpoint, port))
        request = "GET / HTTP/1.0\r\n\r\n"
        try:
            s.sendall(request)
        except socket.error:
            print('Send failed')
    
            
