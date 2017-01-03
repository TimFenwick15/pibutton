# import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM
GPIO.setup(0, GPIO.OUT)

GPIO.output(0, GPIO.HIGH)
GPIO.output(0, GPIO.LOW)

GPIO.cleanup()
