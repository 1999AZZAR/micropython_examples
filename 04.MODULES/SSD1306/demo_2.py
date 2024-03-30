from machine import Pin, I2C
import ssd1306
import time
import math
import urandom

# Initialize I2C and SSD1306 display
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Function to display multiple lines of text
def display_multiple_lines(display, lines):
    for i, line in enumerate(lines):
        display.text(line, 0, i * 12, 1)
    display.show()

# Function to scroll multiple lines of text
def scroll_multiple_lines(display, lines):
    line_height = 12
    max_length = max(len(line) for line in lines)
    for i in range(max_length * 8):
        display.fill(0)
        for j, line in enumerate(lines):
            display.text(line, 0, j * line_height - i % (len(lines) * line_height), 1)
        display.show()
        time.sleep(0.01)

# Function to animate wave effect with scrolling
def wave_scroll_animation(display, lines):
    amplitude = 5
    frequency = 0.1
    line_height = 12
    max_length = max(len(line) for line in lines)
    
    for t in range((max_length + 16) * 8):  # Adjust the range for scrolling
        display.fill(0)
        for j, line in enumerate(lines):
            y_offset = int(amplitude * math.sin(2 * math.pi * frequency * t - j * 2) + j * line_height)
            display.text(line, 0, y_offset - (t % (len(lines) * line_height)), 1)  # Add scrolling effect
        display.show()
        time.sleep(0.01)

# Function to animate diagonal scroll for single line
def diagonal_scroll_single_line(display, text):
    for i in range(128 + len(text) * 8):
        display.fill(0)
        display.text(text, 127 - i, 0, 1)
        display.show()
        time.sleep(0.01)

# Function to animate multiline diagonal scroll
def diagonal_scroll_multiple_lines(display, lines):
    for i in range(128 + max(len(line) for line in lines) * 8):
        display.fill(0)
        for j, line in enumerate(lines):
            display.text(line, 127 - i + j * 16, j * 12, 1)
        display.show()
        time.sleep(0.01)

# Function to animate random blink effect
def random_blink_animation(display, text):
    for _ in range(100):
        display.fill(0)
        if _ % 10 == 0:
            display.text(text, 0, 0, 1)
        display.show()
        time.sleep(0.1)

# Function to animate crossfade effect
def crossfade_animation(display, text1, text2):
    for brightness in range(16):
        display.fill(0)
        display.text(text1, 0, 0, 16 - brightness)
        display.text(text2, 0, 12, brightness)
        display.show()
        time.sleep(0.05)

# Function to animate zoom-in effect
def zoom_in_animation(display, text):
    for i in range(1, 18):
        display.fill(0)
        display.text(text, 64 - 4 * i, 32 - i, 1)
        display.show()
        time.sleep(0.05)

# Function to animate zoom-out effect
def zoom_out_animation(display, text):
    for i in range(17, 0, -1):
        display.fill(0)
        display.text(text, 64 - 4 * i, 32 - i, 1)
        display.show()
        time.sleep(0.05)

# Function to animate jitter effect
def jitter_animation(display, text):
    for _ in range(50):
        display.fill(0)
        display.text(text, urandom.randint(0, 30), urandom.randint(0, 50), 1)
        display.show()
        time.sleep(0.05)

# Pause between demos
time.sleep(2)

# Multiple lines display demo
lines = [
    "This is line 1",
    "This is line 2",
    "This is line 3",
    "This is line 4",
    "This is line 5"
]
display_multiple_lines(display, lines)

# Pause between demos
time.sleep(2)

# Multiple lines scrolling demo
scroll_multiple_lines(display, lines)

# Pause between demos
time.sleep(2)

# Wave effect with scrolling demo
wave_scroll_animation(display, lines)

# Pause between demos
time.sleep(2)

# Diagonal scroll for single line demo
diagonal_scroll_single_line(display, "Diagonal scroll")

# Pause between demos
time.sleep(2)

# Diagonal scroll for multiple lines demo
diagonal_scroll_multiple_lines(display, lines)

# Pause between demos
time.sleep(2)

# Random blink animation demo
random_blink_animation(display, "Blinking")

# Pause between demos
time.sleep(2)

# Crossfade animation demo
crossfade_animation(display, "Hello", "World")

# Pause between demos
time.sleep(2)

# Zoom-in animation demo
zoom_in_animation(display, "Zoom-in")

# Pause between demos
time.sleep(2)

# Zoom-out animation demo
zoom_out_animation(display, "Zoom-out")

# Pause between demos
time.sleep(2)

# Jitter animation demo
jitter_animation(display, "Jitter")

# Pause between demos
time.sleep(2)

# Clear the display
display.fill(0)
display.show()
