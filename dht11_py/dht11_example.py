import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
#instance = dht11.DHT11(pin = 14)
instance = dht11.DHT11(pin = 18)

def get_db18b20():
		tempfile = open("/sys/bus/w1/devices/28-031571bf56ff/w1_slave")
		thetext = tempfile.read()
		tempfile.close
		tempdata = thetext.split("\n")[1].split(" ")[9]
		temperature = float(tempdata[2:])
		temperature = temperature / 1000
		print("db18b20: " , temperature)


while True:
	result = instance.read()
	if result.is_valid():
		print("Last valid input: " + str(datetime.datetime.now()))
		print("Temperature: %d C" % result.temperature)
		print("Humidity: %d %%" % result.humidity)

	get_db18b20()
    		
	time.sleep(2)
