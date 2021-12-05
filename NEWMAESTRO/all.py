import board
import busio
import time
import multiprocessing
import RPi.GPIO as GPIO
import adafruit_bme680
import adafruit_tcs34725
import adafruit_mlx90393
import adafruit_adxl34x


i2c = busio.I2C(board.SCL, board.SDA)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)

bme = adafruit_bme680.Adafruit_BME680_I2C(i2c)
mlx = adafruit_mlx90393.MLX90393(i2c, gain=adafruit_mlx90393.GAIN_1X)
acc = adafruit_adxl34x.ADXL345(i2c)
tcs = adafruit_tcs34725.TCS34725(i2c)

motion = multiprocessing.Value('f', GPIO.input(5))
temperature = multiprocessing.Value('f', bme.temperature)
gas = multiprocessing.Value('f', bme.gas)
humidity = multiprocessing.Value('f', bme.humidity)
pressure = multiprocessing.Value('f', bme.pressure)
MX = multiprocessing.Value('f', mlx.magnetic[0])
MY = multiprocessing.Value('f', mlx.magnetic[1])
MZ = multiprocessing.Value('f', mlx.magnetic[2])
AX = multiprocessing.Value('f', acc.acceleration[0])
AY = multiprocessing.Value('f', acc.acceleration[1])
AZ = multiprocessing.Value('f', acc.acceleration[2])
R = multiprocessing.Value('f', tcs.color_rgb_bytes[0])
G = multiprocessing.Value('f', tcs.color_rgb_bytes[1])
B = multiprocessing.Value('f', tcs.color_rgb_bytes[2])


def getPIR(motion):
    while True:
        motion.value = GPIO.input(5)

def getBME(temperature, gas, humidity, pressure):
    while True:
        temperature.value = bme.temperature
        gas.value = bme.gas
        humidity.value = bme.humidity
        pressure.value = bme.pressure

def getMLX(MX, MY, MZ):
    while True:
        MX.value, MY.value, MZ.value = mlx.magnetic

def getADX(AX, AY, AZ):
    while True:
        AX.value, AY.value, AZ.value = acc.acceleration

def getTCS(R, G, B):
    while True:
        R.value, G.value, B.value = tcs.color_rgb_bytes

p1 = multiprocessing.Process(target=getPIR, args=(motion, )).start()
p2 = multiprocessing.Process(target=getBME, args=(temperature, gas, humidity, pressure, )).start()
p3 = multiprocessing.Process(target=getMLX, args=(MX, MY, MZ, )).start()
p4 = multiprocessing.Process(target=getADX, args=(AX, AY, AZ, )).start()
p5 = multiprocessing.Process(target=getTCS, args=(R, G, B, )).start()


while True:
    time.sleep(0.01)
    print(motion.value, temperature.value, gas.value, humidity.value, pressure.value,
          MX.value, MY.value, MZ.value,
          AX.value, AY.value, AZ.value,
          R.value, G.value, B.value)
