import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)

GPIO.output(31, True)
time.sleep(30)
GPIO.cleanup()
