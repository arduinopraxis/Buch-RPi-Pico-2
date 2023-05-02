# RPi Pico - Webserver
# Datei: buch2-rpi-pico-kap7-webserver-analog.py

#Status: offen


# Bibliotheken
import network
import socket
import time
import machine
  
  
ssid = 'ObiWifinobi'
password = 'crisi7s-stRike-Plus'
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

#Analogeingänge
Analog0 = machine.ADC(26)
Analog1 = machine.ADC(27)
Analog2 = machine.ADC(28)

# HTML Seite - Struktur
html = """<!DOCTYPE html>
    <html>
        <head>
        <meta http-equiv="refresh" content="30">
        <title>RPi Pico W - Webserver</title>
        </head>
        <body>
        <h1>Webserver</h1>
        WerteANALOG
        </body>
    </html>
"""
 
# Verbindungsaufbau
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('Verbindungsaufbau...')
    time.sleep(1)

# Verbindungsfehler/Verbindung
if wlan.status() != 3:
    raise RuntimeError('Fehler: Netzwerkverbindung')
else:
    print('Verbindung OK')
    status = wlan.ifconfig()
    print( 'IP: ' + status[0] )
 
# Socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
 
s = socket.socket()
s.bind(addr)
s.listen(1)
 
stateis = ""
 
# Client-Verbindungen
while True:
    # Analog-Werte einlesen
    valA0 = str(Analog0.read_u16())
    valA1 = str(Analog1.read_u16())
    valA2 = str(Analog2.read_u16())
    valAnalog='A0: '+ valA0 + '<br>'
    valAnalog=valAnalog+'A1: '+ valA1 + '<br>'
    valAnalog=valAnalog+'A2: '+ valA2 + '<br>'

    # Aktualisierung HTML
    response = html.replace('WerteANALOG', valAnalog)

    
    try:
        cl, addr = s.accept()
        print('Client verbunden mit IP: ', addr)
         
   
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
 
    except OSError as e:
        cl.close()
        print('Verbindung geschlossen')