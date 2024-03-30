from machine import Pin, I2C
import ssd1306
import time

# Function to scroll text
def scroll_text(display, lines):
    line_height = 12
    max_length = max(len(line) for line in lines)
    for i in range(max_length * 8):
        display.fill(0)
        for j, line in enumerate(lines):
            display.text(line, 0, j * line_height - i % (len(lines) * line_height), 1)
        display.show()
        time.sleep(0.01)

# Initialize I2C and SSD1306 display
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Multiple lines of text
lines = [
    "This is line 1",
    "This is line 2",
    "This is line 3",
    "This is line 4",
    "This is line 5",
    "This is line 6",
    "This is line 7",
    "This is line 8"
]

# Scroll all lines simultaneously
scroll_text(display, lines)

# Clear the display
display.fill(0)
display.show()
