#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

PIN_REED=5

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_REED, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def getStateReed():
    state= GPIO.input(PIN_REED)
    if state == False:
        print('Reed Detected')
    else:
        print('Reed Not Detected')

# TEST
#getStateReed()
