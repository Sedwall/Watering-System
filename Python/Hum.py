import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.GPIO as GPIO
from time import sleep
from datetime import datetime


def timestamp_value(value):
    dt = datetime.now()
    return "\n" + str(dt) + "\n" + str(value) + "\n"

def calculate_humidty(humidity):
    # An algorithm to get a percentage on the humidity instead of the value given by the sensor
    # The algorithm is gotten from the test values from the different situations (in air/dry soil/wet soil)
    percent_humidity = round((1 - (humidity / 4095)) * 100,1)
    return percent_humidity


def measure_hum():
    hum_measurements = 0
    GPIO.output("P9_12", 1)
    sleep(.1)
    for i in range(0,7):
        value = adc.read_raw("P9_39")
        if i >= 2:
            value = calculate_humidty(value)
            # print((1 - (value / 4095)) * 100)
            print(timestamp_value(value), end="")
            hum_measurements += value
        sleep(3)
    GPIO.output("P9_12", 0)
    return hum_measurements/5

adc.setup()
GPIO.setup("P9_12", GPIO.OUT)
value = adc.read("P9_39")
print(measure_hum())