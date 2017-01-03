# Going to be using the GPIO pins to test getting input from a button.
# The GPIO pins in RPi.GPIO are numbered, 1 to 40.
# Pin 1 is at the top left when the board is orientated portrait with the USB ports at the bottom.

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.IN)

print(GPIO.input(6))
print(GPIO.LOW)
print(GPIO.HIGH)

GPIO.output(5, GPIO.HIGH)

# time.sleep(1)
# if GPIO.input(6):
#   print('Got input')
# if GPIO.input(6):
#   print('Got input')
# if GPIO.input(6):
#   print('Got input')
# if GPIO.input(6):
#   print('Got input')

# print('done')

# while GPIO.input(6) == GPIO.LOW:
#   time.sleep(1)

print('got high') 


# GPIO.output(0, GPIO.LOW)

GPIO.cleanup()
