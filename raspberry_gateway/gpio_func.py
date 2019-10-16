from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
pin_out = 3
GPIO.setup(pin_out, GPIO.OUT)


def toggleSwitch():
    GPIO.output(pin_out, False)
    sleep(0.5)
    GPIO.output(pin_out, True)
