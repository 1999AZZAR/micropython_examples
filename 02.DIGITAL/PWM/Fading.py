from time import sleep
from machine import Pin, PWM

frequency = 5000
led = PWM(Pin(2), frequency)

while True:
    #fade in from min to max in increments of 2 points:
    for fadeValue in range (0, 1023, 2):
        led.duty(fadeValue)
        sleep(0.005)
        #print("min to max: ", fadeValue)
        
    #fade out from max to min in increments of 2 points:
    for fadeValue in range (1023, 0, -2):
        led.duty(fadeValue)
        sleep(0.005)
        #print("max to min: ", fadeValue)
