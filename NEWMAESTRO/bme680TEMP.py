import board
import adafruit_bme680
import busio

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
print(sensor.temperature)
print(sensor.gas)
print(sensor.humidity)
print(sensor.pressure)
