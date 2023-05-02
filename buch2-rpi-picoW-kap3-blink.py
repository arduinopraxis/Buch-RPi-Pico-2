# Pico W - Blink
# Datei: buch2-rpi-picoW-kap3-blink.py

#Bibliotheken
import machine
import utime

#Variablen
led=machine.Pin("LED", machine.Pin.OUT)

#Funktionen

#Loop
while True:
    led.value(1)
    utime.sleep(0.1)
    led.value(0)
    utime.sleep(0.1)
