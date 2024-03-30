from machine import Pin, I2C
import time
import math
import urandom
from ssd1306 import SSD1306_I2C

import machine
machine.freq(160000000) # mcu freq

i2c = I2C(sda=Pin(4), scl=Pin(5)) # i2c pin
oled = SSD1306_I2C(128, 64, i2c)  # display dimensions
oled.contrast(0xFF) # use max brighness

def circle(x, y, r, c):
    diameter = int(r * 2)  # Calculate diameter
    for i in range(-r, r + 1):  # Iterate through the vertical range
        width = int((r ** 2 - i ** 2) ** 0.5)  # Calculate width at this vertical position
        oled.hline(x - width, y + i, 2 * width, c)  # Draw horizontal line at this position

vpos = 31  # Adjust vertical position
EYE = 25  # Increase eye size
PUPIL = 12  # Increase pupil size
TICK = 0.15  # Smaller delay for smoother animation
EXR = 28  # Adjust eye positions
EXL = 100  # Adjust eye positions
WHITE = 1
BLACK = 0

def drawEyes(plh, prh, plv, blink):
    if not blink:
        circle(EXR, vpos, EYE, WHITE)
        circle(EXL, vpos, EYE, WHITE)
        circle(EXR + plh, vpos + plv, PUPIL, BLACK)
        circle(EXL + prh, vpos + plv, PUPIL, BLACK)
    else:
        for i in range(EYE + 2):
            oled.fill_rect(EXR - EYE + i, vpos - EYE + i, (EYE - i) * 2, (EYE - i) * 2, BLACK)
            oled.fill_rect(EXL - EYE + i, vpos - EYE + i, (EYE - i) * 2, (EYE - i) * 2, BLACK)

def displayTick():
    oled.show()
    time.sleep(TICK)

def centerDraw(blink):
    drawEyes(0, 0, 0, blink)

def center(blink):
    centerDraw(blink)
    displayTick()

def left(blink):
    drawEyes(-6, -6, 0, blink)
    displayTick()

def up(blink):
    drawEyes(1, -1, -6, blink)
    displayTick()

def down(blink):
    drawEyes(1, -1, 6, blink)
    displayTick()

def right(blink):
    drawEyes(6, 6, 0, blink)
    displayTick()

def rollEyes():
    center(False)
    left(False)
    up(False)
    right(False)
    center(False)

def lookLeft():
    left(False)
    center(False)

def lookRight():
    right(False)
    center(False)

def lookUp():
    up(False)
    center(False)

def lookDown():
    down(False)
    center(False)

while True:
    action = urandom.getrandbits(5)  # Generate random action
    #print(action)

    if action == 1:
        lookRight()
    elif action == 2:
        lookUp()
    elif action == 3:
        lookDown()
    elif action == 4:
        lookLeft()
    elif action == 5:
        rollEyes()
    elif action == 6:
        up(False)
    elif action == 7:
        down(False)
    elif action == 8:
        left(False)
    elif action == 9:
        right(False)

    # Randomly include blinking action with each other action
    if urandom.getrandbits(5) < 6:  # Adjust the threshold for blinking frequency
        center(True)

    center(False)
