# RPi Pico - Webclient
# Datei: buch2-rpi-pico-kap7-webclient.py

#Bibliotheken
import network
import urequests
import utime

#WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('MeinWLan',','MeinPasswort')

while not wlan.isconnected() and wlan.status() >= 0:
    print("Verbinden...")
    utime.sleep(1)

wstat=wlan.status()
print(wstat)

#Webaufruf
response = urequests.get("https://555circuitslab.com/files/buch-rpi-pico.xml")
print(response.content)
response.close()
