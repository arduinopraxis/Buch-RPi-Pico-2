# RPi Pico - RTC mit DS3231
# Datei: buch2-rpi-pico-kap6-rtc-ds3231.py

#Bibliotheken
import ds3231
import utime

# Initialisierung
rtc = ds3231.RTC(sda_pin=8, scl_pin=9)

# Zeit lesen und ausgeben
rtc_time = rtc.ReadTime('DIN-1355-1+time')
print(rtc_time)

# Zeit setzen: Sekunde / Minute / Stunde / Wochentag / Tag / Monat / Jahr
#rtc.SetTime(b'\x00\x34\x17\x04\x12\x10\x22')


while True:
    rtc_time = rtc.ReadTime('DIN-1355-1+time')
    print(rtc_time)
    utime.sleep(1)
    

