#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
from datetime import datetime, timedelta
from time import sleep

# Setup GPIO
GPIO.setup("P9_14", GPIO.OUT)


def get_time() -> datetime:
    # Add 2 hours to the GMT time to get local time
    now = datetime.now()
    return now + timedelta(hours=2)

def water(duration = 2):
    print("Start", get_time())
    GPIO.output("P9_14", GPIO.HIGH)
    sleep(duration)
    GPIO.output("P9_14", GPIO.LOW)
    print("Done")


while True:
    # Every hour
    if get_time().hour == 17:
        water()
    sleep(60 * 2) 