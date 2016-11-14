Script for gathering temp and humidity readings from AS2302 in a format that Prometheus can process.


###Installation:###

git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT

sudo apt-get install build-essential python-dev

sudo python setup.py install

###Example output###

```
node_sensor_temp{node="sensor.example.com",location="somewhere",sensor="am2302"} 22.3
node_sensor_humidity{node="sensor.example.com",location="somewhere",sensor="am2302"} 35.3
node_sensor_updated_timestamp{node="sensor.example.com"} 1479072202
```
