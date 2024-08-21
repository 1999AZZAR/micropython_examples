from machine import Pin, I2C
import ssd1306
import time

# using default address 0x3C
i2c = I2C(sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Long text for scrolling
line1 = "This is a long text for scrolling example. Hello, MicroPython!"

# Scroll the text
for i in range(len(line1) * 8):
    display.fill(0)
    display.text(line1, -i, 3, 1)
    display.show()
    time.sleep(0.01)

# Wait for a moment
time.sleep(0.5)

# Clear the display
display.fill(0)
display.show()
