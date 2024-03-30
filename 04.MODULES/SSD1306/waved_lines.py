from machine import Pin, I2C
import ssd1306
import time
import math

# Function to animate wave effect with scrolling
def wave_scroll_animation(display, lines):
    amplitude = 4
    frequency = 0.05
    line_height = 12
    max_length = max(len(line) for line in lines)
    
    for t in range((max_length + 16) * 8):  # Adjust the range for scrolling
        display.fill(0)
        for j, line in enumerate(lines):
            y_offset = int(amplitude * math.sin(2 * math.pi * frequency * t - j * 2) + j * line_height)
            display.text(line, 0, y_offset - (t % (len(lines) * line_height)), 1)  # Add scrolling effect
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

# Animate wave effect with scrolling
wave_scroll_animation(display, lines)

# Clear the display
display.fill(0)
display.show()
