#!/usr/bin/python


import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT) # RED
GPIO.setup(38, GPIO.OUT) # GREEN
GPIO.setup(40, GPIO.OUT) # BLUE

for i in range(10):
    GPIO.output(36,True)
    time.sleep(1)
    GPIO.output(36,False)
    time.sleep(1)
    GPIO.output(38,True)
    time.sleep(1)
    GPIO.output(38,False)
    time.sleep(1)
    GPIO.output(40,True)
    time.sleep(1)
    GPIO.output(40,False)
    time.sleep(1)
    
GPIO.cleanup()

