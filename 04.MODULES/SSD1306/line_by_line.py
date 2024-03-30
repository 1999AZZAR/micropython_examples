from machine import Pin, I2C
import ssd1306
import time

# Function to display text line by line
def display_lines(display, lines):
    for i, line in enumerate(lines):
        display.fill(0)  # Clear the display
        display.text(line, 0, i * 12, 1)  # Display the line
        display.show()  # Update the display
        time.sleep(1)  # Pause for 1 second

# Initialize I2C and SSD1306 display
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Multiple lines of text
lines = [
    "This is line 1",
    "This is line 2",
    "This is line 3",
    "This is line 4",
    "This is line 5"
]

# Display each line one after another
display_lines(display, lines)

# Clear the display
display.fill(0)
display.show()
