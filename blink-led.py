#!/usr/bin/python


import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

for i in range(10):
    GPIO.output(12,True)
    time.sleep(1)
    GPIO.output(12,False)
    time.sleep(1)
    
GPIO.cleanup()

