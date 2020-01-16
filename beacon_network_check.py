import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
IP = "8.8.8.8"

response = os.system("ping -c 1 " + IP)

if response == 0:
  GPIO.output(31, False)
  GPIO.cleanup()
else:
  time.sleep(5)
  response = os.system("ping -c 1 " + IP)
if response!=0:
  GPIO.output(31, True)
  time.sleep(30)
  GPIO.cleanup()
else:
  GPIO.output(31, False)
  GPIO.cleanup()
