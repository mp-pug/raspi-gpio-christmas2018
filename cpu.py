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
    if usage < 30 :
        dim(red_led,0)
        dim(green_led,0)
        dim(blue_led,100)
    elif usage >= 30 and usage < 80:
        dim(red_led,0)
        dim(blue_led,0)
        dim(green_led,100)
    else:
        dim(green_led,0)
        dim(blue_led,0)
        dim(red_led,100)
    
    time.sleep(1)
    
GPIO.cleanup()

