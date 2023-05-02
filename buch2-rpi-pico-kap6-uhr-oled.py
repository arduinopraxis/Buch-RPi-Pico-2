# RPi Pico - Uhr mit OLED
# Datei: buch2-rpi-pico-kap6-uhr-oled.py

#Bibliotheken
import ds3231
from ssd1306 import SSD1306_I2C
import utime

# I2C
sda=machine.Pin(8)
scl=machine.Pin(9)
i2c = machine.I2C(0, scl=scl, sda=sda, freq=100000)

# OLED
oled = SSD1306_I2C(128, 32, i2c)

# Initialisierung
rtc = ds3231.RTC(sda_pin=8, scl_pin=9)

# Zeit lesen und ausgeben
rtc_time = rtc.ReadTime('DIN-1355-1+time')
print(rtc_time)

# Zeit setzen: Sekunde / Minute / Stunde / Wochentag / Tag / Monat / Jahr
#rtc.SetTime(b'\x00\x34\x17\x04\x12\x10\x22')


while True:
    rtc_uhr = rtc.ReadTime('time')
    oled.text(rtc_uhr, 10, 20)
    oled.show()
    utime.sleep(1)
    oled.fill(0)
    

