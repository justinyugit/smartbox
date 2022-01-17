import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN)

while(True):
    time.sleep(.5)
    i = GPIO.input(29)
    print(i)
