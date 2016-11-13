#!/usr/bin/python
import Adafruit_DHT
import time
import socket
import os

sensor = Adafruit_DHT.DHT22
pin = 4
tid = time.time()
node = socket.getfqdn()
location = "somewhere"

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    with open('am2302sensor', 'w+') as f:
        f.write('as_2302_temp{{node="{0}",location="{2}"}} {1:0.1f}\n'.format(node, temperature, location))
        f.write('as_2302_humidity{{node="{0}",location="{2}"}} {1:0.1f}\n'.format(node, humidity, location))
        f.write('as_2302_updated_timestamp{{node="{0}"}} {1:.0f}\n'.format(node, tid))
	f.close()
