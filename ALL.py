'''
Multithreading i2c sensor readings.
Written by Justin Yu
December 2020
'''

import board
import busio
import adafruit_bno055
import adafruit_bme280
import time
import threading
i2c = busio.I2C(board.SCL, board.SDA)
bno = adafruit_bno055.BNO055_I2C(i2c)
bme = adafruit_bme280.Adafruit_BME280_I2C(i2c)


### BME280 Readings ###

temperature = None
humdity = None
pressure = None
altitude = None

#######################

