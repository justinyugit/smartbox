'''
Multiprocessing i2c sensor readings.
Written by Justin Yu
December 2020
'''

import board
import busio
import adafruit_bno055
import adafruit_bme280
import adafruit_tcs34725
import time
import multiprocessing
import RPi.GPIO as GPIO

i2c = busio.I2C(board.SCL, board.SDA)
bno = adafruit_bno055.BNO055_I2C(i2c)
bme = adafruit_bme280.Adafruit_BME280_I2C(i2c)
tcs = adafruit_tcs34725.TCS34725(i2c)
manager = multiprocessing.Manager()
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.IN)

t_end = time.time() + 10 # Seconds
bme.sea_level_pressure = 1045 # Calibration purposes


### BME280 Readings ### 
temperature = multiprocessing.Value('f', (bme.temperature))
humidity = multiprocessing.Value('f', (bme.humidity))
pressure = multiprocessing.Value('f', (bme.pressure))
altitude = multiprocessing.Value('f', (bme.altitude))

### BNO055 Readings ###
acceleration = manager.list(list(bno.acceleration))
magnetic = manager.list(list(bno.magnetic))
gyro = manager.list(list(bno.gyro))

### TCS34725 Readings ###
rgb = manager.list(list(tcs.color_rgb_bytes))
colorT = multiprocessing.Value('f',tcs.color_temperature)
lux = multiprocessing.Value('f',tcs.lux)

### PIR Readings ###
motion = multiprocessing.Value('f', GPIO.input(36))

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
        

def getTCS(rgb, colorT, lux):
    while time.time() < t_end:
        rgb[0] = tcs.color_rgb_bytes
        colorT.value = tcs.color_temperature
        lux.value = tcs.lux

def getPIR(motion):
    while time.time() < t_end:
        motion=GPIO.input(36)

p1 = multiprocessing.Process(target=getBME, args=(temperature, humidity, pressure, altitude, )).start()
p2 = multiprocessing.Process(target=getBNO, args=(acceleration, magnetic, gyro, )).start()
p3 = multiprocessing.Process(target=getTCS, args=(rgb, colorT, lux, )).start()
p4 = multiprocessing.Process(target=getPIR, args=(motion, )).start()
time.sleep(0.1)

output = []
while time.time()<t_end:
    if(temperature and
       humidity and
       pressure and
       altitude and
       len(acceleration)==3 and
       len(magnetic)==3 and
       len(gyro)==3):
        output.append({motion.value, temperature.value, humidity.value, pressure.value, altitude.value, acceleration[0], magnetic[0], gyro[0], rgb[0], colorT.value, lux.value})

print(len(output))
