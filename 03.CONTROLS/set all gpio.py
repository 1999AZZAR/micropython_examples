from machine import Pin

# List of available GPIO pins on ESP32 (excluding those used for other purposes)
# Typically, GPIO 1 and 3 are used for UART and might not be available for general use.
gpio_pins = [0, 2, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 32, 33]

# Initialize all GPIO pins as outputs and set them high, then print their status
def set_up_all_gpios():
    for pin in gpio_pins:
        p = Pin(pin, Pin.OUT)
        p.value(0)  # Set the pin high
        print(f'GPIO {pin} is set to {p.value()}')

# Main function
def main():
    set_up_all_gpios()

if __name__ == "__main__":
    main()
