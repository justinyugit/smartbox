'''
Multiprocessing i2c sensor readings.
Written by Justin Yu
December 2020
'''

import board
import busio
import adafruit_bno055
import adafruit_bme280
import time
import multiprocessing
import ctypes
from ctypes import c_wchar_p

i2c = busio.I2C(board.SCL, board.SDA)
bno = adafruit_bno055.BNO055_I2C(i2c)
bme = adafruit_bme280.Adafruit_BME280_I2C(i2c)
manager = multiprocessing.Manager()

t_end = time.time() + 2
bme.sea_level_pressure = 1045

### BME280 Readings ### 
temperature = multiprocessing.Value('f', (bme.temperature))
humidity = multiprocessing.Value('f', (bme.humidity))
pressure = multiprocessing.Value('f', (bme.pressure))
altitude = multiprocessing.Value('f', (bme.altitude))


### BNO055 Readings ###
acceleration = manager.list(list(bno.acceleration))
magnetic = manager.list(list(bno.magnetic))
gyro = manager.list(list(bno.gyro))



def getBME(temperature, humidity, pressure, altitude):
    while time.time() < t_end:
        temperature.value = (bme.temperature)
        humidity.value = (bme.relative_humidity)
        pressure.value = (bme.pressure)
        altitude.value = (bme.altitude)

        

def getBNO(acceleration, magnetic, gyro):
    while time.time() < t_end:
        acceleration[0] = bno.acceleration
        magnetic[0] = bno.magnetic
        gyro[0] = bno.gyro
        

p1 = multiprocessing.Process(target=getBME, args=(temperature, humidity, pressure, altitude, )).start()
p2 = multiprocessing.Process(target=getBNO, args=(acceleration, magnetic, gyro, )).start()
while time.time()<t_end:
    if(temperature and
       humidity and
       pressure and
       altitude and
       acceleration and
       magnetic and
       gyro):
        print(temperature.value, humidity.value, pressure.value, altitude.value, acceleration[0], magnetic[0], gyro[0])
