import machine
import time

class Blinker:
    """
    A class to control an LED blink pattern using MicroPython.
    """
    
    def __init__(self, pin=2):
        """
        Initialize the Blinker with a specified LED pin.
        
        :param pin: The GPIO pin number where the LED is connected. Default is 2.
        """
        self.led = machine.Pin(pin, machine.Pin.OUT)
        
    def blink(self, num_blinks, on_duration, off_duration):
        """
        Blink the LED a specified number of times with given on and off durations.
        
        :param num_blinks: Number of times the LED should blink.
        :param on_duration: Duration (in seconds) the LED stays on.
        :param off_duration: Duration (in seconds) the LED stays off.
        """
        for _ in range(num_blinks):
            self.led.value(not self.led.value())
            time.sleep(on_duration)
            self.led.value(not self.led.value())
            time.sleep(off_duration)

# Example usage:
# blinker = Blinker(2)
# blinker.blink(5, 0.5, 0.5)
