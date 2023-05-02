# Pico/Pico W - interner RTC
# Datei: buch2-rpi-picoW-kap6-rtc.py

#Bibliotheken
import machine
import utime

# RTC Initialisierung
rtc = machine.RTC()

#Uhrzeit setzen
rtc.datetime((2022, 10, 05, 4, 10, 56, 0, 0))

#Loop
while True:
    print(rtc.datetime())
    utime.sleep(1)
