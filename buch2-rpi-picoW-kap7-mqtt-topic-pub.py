# Raspberry Pi Pico - MQTT Client PubSub
# Datei: buch2-rpi-picoW-kap7-mqtt-topic-pub.py

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
topic_pub = "RPIPico"
topic_msg = "Hello Pico..."

#Funktionen
def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.connect()
    print('Verbunden mit %s MQTT Broker'%(mqtt_server))
    return client

def callback(topic, msg):
    t = topic.decode("utf-8").lstrip(topic)
    print(t)  

def reconnect():
    print('Fehler beim Verbinden mit MQTT Broker. Verbindungsaufbau...')
    time.sleep(5)

#MQTT Loop
try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
while True:
    client = mqtt_connect()
    client.publish(topic_pub, topic_msg)
    client.set_callback(callback)
    time.sleep(3)
    client.disconnect()