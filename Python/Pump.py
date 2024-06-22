#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
from time import sleep


def duration():
    i = input("Duration: ")
    try:
        i = int(i)
    except:
        print("...")
    if i in range(0,10):
        duration = i
    else:
        print("Wrong input, try agan..\n\n")
        i = duration()
    return i
    



GPIO.setup("P9_14", GPIO.OUT)
duration = duration()
print("Start")
GPIO.output("P9_14", GPIO.HIGH)
sleep(duration)
GPIO.output("P9_14", GPIO.LOW)
print("Done")
#hej