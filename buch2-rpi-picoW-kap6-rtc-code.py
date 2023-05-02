#Bibliotheken
import machine
rtc = machine.RTC()
# Uhrzeit setzen
rtc.datetime((2022, 10, 05, 4, 10, 56, 0, 0))
print(rtc.datetime())
