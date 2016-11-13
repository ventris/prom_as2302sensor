#!/usr/bin/python
import Adafruit_DHT
import time
import socket

sensor = Adafruit_DHT.DHT22
pin = 4
tid = time.time()
node = socket.getfqdn()

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('as_2302_temp{{node="{0}",location="oland"}} {1:0.1f}'.format(node, temperature))
    print('as_2302_humidity{{node="{0}",location="oland"}} {1:0.1f}'.format(node, humidity))
    print('as_2302_updated_timestamp{{node="{0}"}} {1:.0f}'.format(node, tid))
