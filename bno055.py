import board
import busio
import adafruit_bno055
import time
import threading
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

temp = []
acc = []
mag = []
gyr = []
eul = []
qua = []
linacc = []
grav = []
t_end = time.time() + 10

def getTemperature():
    while time.time() < t_end:
        a = sensor.temperature
        if (a>0):
            temp.append(a)
            print(a)

def getAcceleration():
    while time.time() < t_end:
        b = sensor.acceleration
        acc.append(b)


def getMagnetic():
    while time.time() < t_end:
        c = sensor.magnetic
        mag.append(c)
    
def getGyro():
    while time.time() < t_end:
        b = sensor.acceleration
        c = sensor.magnetic
        d = sensor.gyro
        gyr.append(d)
        mag.append(c)
        acc.append(b)
    
    
def getEuler():
    while time.time() < t_end:
        e = sensor.euler
        eul.append(e)
    


print(len(temp))
print(len(acc))
print(len(mag))
print(len(gyr))
print(len(eul))
