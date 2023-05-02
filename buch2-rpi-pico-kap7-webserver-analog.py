# RPi Pico - Webserver
# Datei: buch2-rpi-pico-kap7-webserver-analog.py

# Bibliotheken
import network
import ubinascii
import machine
import urequests as requests
import time
from secrets import secrets
import socket

# WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# MAC Adresse
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print('mac = ' + mac)

# WLAN Login
ssid = secrets['ssid']
pw = secrets['pw']
wlan.connect(ssid, pw)

#Analogeingänge
Analog0 = machine.ADC(26)
Analog1 = machine.ADC(27)
Analog2 = machine.ADC(28)

# Warten Verbindungsaufbau
timeout = 10
while timeout > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    timeout -= 1
    print('Verbindungsaufbau...')
    time.sleep(1)
    

if wlan.status() != 3:
    raise RuntimeError('Verbindung fehlgeschlagen!')
else:
    print('Verbunden...')
    status = wlan.ifconfig()
    print('IP: ' + status[0])
    
# HTML Seite laden    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()     
    return html


# HTTP Server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('Listening on', addr)

# Verbindung 
while True:
    try:
        cl, addr = s.accept()
        print('Client verbunden von: ', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
            
        response = get_html('index-sensor-chart.html')
        
        # Analog-Werte einlesen
        valA0 = str(Analog0.read_u16())
        valA1 = str(Analog1.read_u16())
        valA2 = str(Analog2.read_u16())
 
        response = response.replace('vA0', valA0)
        response = response.replace('vA1', valA1)
        response = response.replace('vA2', valA2)     
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
    except OSError as e:
        cl.close()
        print('Connection closed')