# import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
out_pin = 3
GPIO.setup(out_pin, GPIO.OUT)

def toggleSwitch():
   GPIO.output(out_pin, False)
   GPIO.output(out_pin, True)
