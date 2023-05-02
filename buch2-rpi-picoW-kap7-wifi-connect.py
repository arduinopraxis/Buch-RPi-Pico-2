# RPi Pico - Wifi Connect
# Datei: buch2-rpi-picoW-kap7-wifi-connect.py

# Bibliotheken

import network
import utime

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('MeinWLAN','MeinPasswort')

while not wlan.isconnected() and wlan.status() >= 0:
    print("Verbinden...")
    utime.sleep(1)

print(wlan.status())
print(wlan.ifconfig())    
