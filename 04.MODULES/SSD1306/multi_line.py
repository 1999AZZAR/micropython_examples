from machine import Pin, I2C
import ssd1306
import time

# using default address 0x3C
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Display multiple lines of text
display.text('Hello, MicroPython!', 0, 3, 1)
display.text('This is a', 0, 15, 1)
display.text('Multi-line Example', 0, 27, 1)

# Update the OLED display
display.show()

# Wait for a moment
time.sleep(7)

# Clear the display
display.fill(0)
display.show()
