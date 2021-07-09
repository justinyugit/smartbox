import board
import busio

import adafruit_tcs34725
import time

import RPi.GPIO as GPIO

i2c = busio.I2C(board.SCL, board.SDA)

tcs = adafruit_tcs34725.TCS34725(i2c)

rgb = tcs.color_rgb_bytes
print(rgb)
