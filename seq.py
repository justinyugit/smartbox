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

t_end = time.time() + 1
bme.sea_level_pressure = 1045

### BME280 Readings ###

temperature = None
humidity = None
pressure = None
altitude = None


### BNO055 Readings ###

acceleration = None
magnetic = None
gyro = None

count = 0

def getBME():
    global temperature
    global humidity
    global pressure
    global altitude
    global count
    temperature = bme.temperature
    humidity = bme.relative_humidity
    pressure = bme.pressure
    altitude = bme.altitude
    count = count+1
        
def getBNO():
    global acceleration
    global magnetic
    global gyro
    global count
    acceleration = bno.acceleration
    magnetic = bno.magnetic
    gyro = bno.gyro
    count=count+1



def one():
    while time.time() < t_end:
        getBME()

def two():
    while time.time() < t_end:
        getBNO()
t1 = threading.Thread(target=one)
#t2 = threading.Thread(target=two)
t1.start()
#t2.start()
while time.time() < t_end:
    print(temperature, humidity, pressure, altitude, acceleration, magnetic, gyro)
    
print(count)
    #t1.join()
#getBNO()

