import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.GPIO as GPIO
from Remote_uppdate import send_message, get_message
from datetime import datetime
from time import sleep
import os 


save_path = os.getcwd() + "/Hum.txt"
adc.setup()
GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_14", GPIO.OUT)
value = adc.read("P9_40")


def calculate_humidty(humidity):
    # An algorithm to get a percentage on the humidity instead of the value given by the sensor
    # The algorithm is gotten from the test values from the different situations (in air/dry soil/wet soil)
    percent_humidity = round((1 - (humidity / 4095)) * 100,1)
    return percent_humidity


def timestamp_value(value):
    dt = datetime.now()
    return "\n" + str(dt) + "\n" + str(value) + "\n"


def measure_hum():

    hum_measurements = 0

    GPIO.output("P9_12", 1)
    sleep(3)
    for i in range(0,5):
        value = adc.read_raw("P9_40")
        value = calculate_humidty(value)
        # print((1 - (value / 4095)) * 100)
        print(timestamp_value(value), end="")
        hum_measurements += value
        sleep(3)
    GPIO.output("P9_12", 0)
    return hum_measurements/5

def save_data(hum_str):
    # the old data is retrived
    try:
        Data = open(save_path, "r").read()
    except:
        Data = ""
    # new data is added
    data_save = Data + hum_str
    # old + new data is written back in to the text file
    Data = open(save_path, "w")
    Data.write(data_save)
    Data.close()


def pump(sec):
    GPIO.output("P9_14", 1)
    sleep(sec)
    GPIO.output("P9_14", 0)



old_message = get_message()
sleep(60)

while True:
    new_message = get_message()
    if new_message.id != old_message.id:
        print("New message resived...")
        # tar ut texten
        message = new_message.message_create["message_data"]["text"]
        if message == "Hum":
            #om texten = hum, mät hum och skicka tillbacka värdet
            hum = timestamp_value(measure_hum())
            send_message(hum)
            save_data(hum)
        elif message.split(" ")[0] == "Pump:":
            try:
                sec = int(message.split(" ")[1])
                if sec in [1, 2, 3, 4, 5]:
                    print("Message: ", sec)
                    pump(sec)
                    sleep(30)
                    hum = timestamp_value(measure_hum())
                    send_message(hum)
                    save_data(hum)
                else:
                    print("Message not correct format..." )
            except:
                print("Message not correct format..." )
            sleep(30)
        old_message = get_message()
    print("...")
    sleep(60) 