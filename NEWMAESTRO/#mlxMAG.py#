import time
import board
import adafruit_mlx90393

i2c = board.I2C()
SENSOR = adafruit_mlx90393.MLX90393(i2c, gain=adafruit_mlx90393.GAIN_1X)

MX, MY, MZ = SENSOR.magnetic
print(MX, MY, MZ)
