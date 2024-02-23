from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO


GPIO.setup(26, 'output')

# Switch on
GPIO.output(26, GPIO.HIGH)

# To read the state
state = GPIO.input(26)
if state:
   print('on')
else:
   print('off')

#led = LED(26)

#lled.on()
#led.off()
# while True:
    # led.on()
    # sleep(5)
    # led.off()
    # sleep(5)
    
