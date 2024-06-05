# Blink Example in MicroPython

import machine
import time

# Define the pin number where the LED is connected
led_pin = 2  # Change this to the appropriate pin on your board

# Set up the LED pin as an output
led = machine.Pin(led_pin, machine.Pin.OUT)

# Function to blink the LED
def blink_led(duration_sec, blink_interval_sec):
    num_blinks = int(duration_sec / (2 * blink_interval_sec))
    
    for _ in range(num_blinks):
        led.on()   # Turn on the LED
        time.sleep(blink_interval_sec)
        led.off()  # Turn off the LED
        time.sleep(blink_interval_sec)

# Example: Blink the LED for 100 seconds with a 0.07-second interval
blink_led(10, 0.05)
