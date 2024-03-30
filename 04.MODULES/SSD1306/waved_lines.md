# Wave Animation Readme

This Python code demonstrates how to animate a wave effect on an SSD1306 OLED display using a microcontroller, such as an ESP32 or ESP8266, with MicroPython.

## Dependencies

- `machine`: This module provides functions for controlling hardware components, such as pins and I2C.
- `ssd1306`: This module enables communication with the SSD1306 OLED display over I2C.
- `time`: This module provides various time-related functions.
- `math`: This module is used for mathematical operations, specifically to generate the wave effect.

## Installation

Ensure that MicroPython is installed on your microcontroller. Then, copy the provided code into a `.py` file on the microcontroller.

## Usage

1. Connect the SSD1306 OLED display to the microcontroller using the I2C protocol.
2. Adjust the pin numbers for the SDA and SCL lines in the code if necessary.
3. Execute the code on the microcontroller.
4. Watch as the wave effect animates on the OLED display with the provided text lines.

## Functionality

The code defines a function `wave_scroll_animation` that animates a wave effect with scrolling on the SSD1306 display. The parameters include the display object and a list of text lines to display. The animation creates a wave-like motion across the lines of text, giving a visually appealing effect.

## Usage Example

```python
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
```

## Notes

- Ensure that the correct pin numbers are used for SDA and SCL lines based on your hardware setup.
- Adjust the animation parameters (amplitude, frequency) in the `wave_scroll_animation` function to customize the effect.
- This code is specifically tailored for MicroPython and may require modifications for other platforms or languages.

