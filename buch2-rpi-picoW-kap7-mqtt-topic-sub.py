# Raspberry Pi Pico - MQTT Client PubSub
# Datei: buch2-rpi-picoW-kap7-mqtt-topic-sub.py

# Bibliothek
import time
import network
from umqttsimple import MQTTClient
import urequests

#WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('MeinWLAN','MeinPasswort')

#MQTT Konfiguration
mqtt_server = '192.168.1.42'
client_id = 'pico'
topic_sub = b'RPIPicoSensor'

#Funktionen
def sub_cb(topic, msg):
    print("Neue Daten von Topic {}".format(topic.decode('utf-8')))
    msg = msg.decode('utf-8')
    print(msg)
    

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.set_callback(sub_cb)
    client.connect()
    print('Verbunden mit %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Fehler beim Verbinden mit MQTT Broker. Verbindungsaufbau...')
    time.sleep(5)
    
#MQTT Loop
try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
while True:
    client.subscribe(topic_sub)
    time.sleep(1)