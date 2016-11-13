Script for gathering temp and humidity readings from AS2303 in a format that Prometheus can process.


###Installation:###

git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT

sudo apt-get install build-essential python-dev

sudo python setup.py install

###Example output###

```
as_2302_temp{node="sensor.example.com",location="somewhere"} 22.3
as_2302_humidity{node="sensor.example.com",location="somewhere"} 35.3
as_2302_updated_timestamp{node="sensor.example.com"} 1479072202
```
