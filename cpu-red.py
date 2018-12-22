#!/usr/bin/python


import RPi.GPIO as GPIO
import time
import psutil

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT) # RED
GPIO.setup(38, GPIO.OUT) # GREEN
GPIO.setup(40, GPIO.OUT) # BLUE

red_led= GPIO.PWM(36,100)
green_led=GPIO.PWM(38,100)
blue_led=GPIO.PWM(40,100)



red_led.start(0)
green_led.start(0)
blue_led.start(0)




def dim ( led, value ):
    led.ChangeDutyCycle(value)
    time.sleep(0.05)







while True:
    usage=psutil.cpu_percent()
    dim(red_led,usage)
    time.sleep(1)
    
GPIO.cleanup()

