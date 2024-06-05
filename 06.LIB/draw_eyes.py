# eye.py

from machine import Pin, I2C
import time
import urandom
from ssd1306 import SSD1306_I2C
import machine

class EyeAnimation:
    def __init__(self):
        machine.freq(160000000)  # Set MCU frequency to maximum
        self.i2c = I2C(sda=Pin(4), scl=Pin(5))
        self.oled = SSD1306_I2C(128, 64, self.i2c)
        self.oled.contrast(0xFF)  # Set OLED brightness to maximum
        self.vpos = 31 # eye position (middle)
        self.EYE_MAJOR_AXIS = 20 # the eye vertical size
        self.EYE_MINOR_AXIS = 25 # the eye horizontal size
        self.PUPIL_MAJOR_AXIS = 12 # the pupil vertical size
        self.PUPIL_MINOR_AXIS = 9 # the pupil horizontal size
        self.TICK = 0.15
        self.EXR = 30 # left eye fist position
        self.EXL = 98 # right eye first position
        self.WHITE = 1
        self.BLACK = 0

    def ellipse(self, x, y, a, b, c):
        for i in range(-a, a + 1):
            width = int(((1 - (i / a) ** 2) * b ** 2) ** 0.5)
            self.oled.hline(x - width, y + i, 2 * width, c)

    def drawEyes(self, plh, prh, plv, blink):
        if blink:
            self.ellipse(self.EXR, self.vpos, self.EYE_MAJOR_AXIS, self.EYE_MINOR_AXIS, self.BLACK)
            self.ellipse(self.EXL, self.vpos, self.EYE_MAJOR_AXIS, self.EYE_MINOR_AXIS, self.BLACK)
        else:
            # Draw outer eye ellipse
            self.ellipse(self.EXR, self.vpos, self.EYE_MAJOR_AXIS, self.EYE_MINOR_AXIS, self.WHITE)
            self.ellipse(self.EXL, self.vpos, self.EYE_MAJOR_AXIS, self.EYE_MINOR_AXIS, self.WHITE)
            # Draw pupil ellipse inside the eye
            self.ellipse(self.EXR + plh, self.vpos + plv, self.PUPIL_MAJOR_AXIS, self.PUPIL_MINOR_AXIS, self.BLACK)
            self.ellipse(self.EXL + prh, self.vpos + plv, self.PUPIL_MAJOR_AXIS, self.PUPIL_MINOR_AXIS, self.BLACK)

    def displayTick(self):
        self.oled.show()
        time.sleep(self.TICK)

    def centerDraw(self, blink):
        self.drawEyes(0, 0, 0, blink)

    def center(self, blink):
        self.centerDraw(blink)
        self.displayTick()

    def left(self, blink):
        self.drawEyes(-6, -6, 0, blink)
        self.displayTick()

    def up(self, blink):
        self.drawEyes(1, -1, -6, blink)
        self.displayTick()

    def down(self, blink):
        self.drawEyes(1, -1, 6, blink)
        self.displayTick()

    def right(self, blink):
        self.drawEyes(6, 6, 0, blink)
        self.displayTick()

    def rollEyes(self):
        self.center(False)
        self.left(False)
        self.up(False)
        self.right(False)
        self.center(False)

    def lookLeft(self):
        self.left(False)
        self.center(False)

    def lookRight(self):
        self.right(False)
        self.center(False)

    def lookUp(self):
        self.up(False)
        self.center(False)

    def lookDown(self):
        self.down(False)
        self.center(False)

    def animate(self):
        while True:
            action = urandom.getrandbits(5)
            if action == 1:
                self.lookRight()
            elif action == 2:
                self.lookUp()
            elif action == 3:
                self.lookDown()
            elif action == 4:
                self.lookLeft()
            elif action == 5:
                self.rollEyes()
            elif action == 6:
                self.up(False)
            elif action == 7:
                self.down(False)
            elif action == 8:
                self.left(False)
            elif action == 9:
                self.right(False)

            if urandom.getrandbits(5) < 6:  # Adjust the threshold for blinking frequency
                self.center(True)

            self.center(False)

