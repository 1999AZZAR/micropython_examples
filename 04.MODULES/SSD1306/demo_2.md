# SSD1306 Display Animation Demos Readme

This Python code demonstrates various animations and effects on an SSD1306 OLED display using MicroPython.

## Dependencies

- `machine`: This module provides functions for controlling hardware components, such as pins and I2C.
- `ssd1306`: This module enables communication with the SSD1306 OLED display over I2C.
- `time`: This module provides various time-related functions.
- `math`: This module is used for mathematical operations, specifically for wave animation.
- `urandom`: This module generates random numbers, used for randomizing animations.

## Installation

Ensure that MicroPython is installed on your microcontroller. Then, copy the provided code into a `.py` file on the microcontroller.

## Usage

1. Connect the SSD1306 OLED display to the microcontroller using the I2C protocol.
2. Adjust the pin numbers for the SDA and SCL lines in the code if necessary.
3. Execute the code on the microcontroller.
4. Observe the OLED display as it demonstrates various animations and effects.

## Animations and Effects

- **Multiple Lines Display Demo**: Displays multiple lines of text on the OLED display.
- **Multiple Lines Scrolling Demo**: Scrolls multiple lines of text vertically on the OLED display.
- **Wave Effect with Scrolling Demo**: Animates a wave effect while scrolling multiple lines of text.
- **Diagonal Scroll for Single Line Demo**: Scrolls a single line of text diagonally across the OLED display.
- **Diagonal Scroll for Multiple Lines Demo**: Scrolls multiple lines of text diagonally across the OLED display.
- **Random Blink Animation Demo**: Simulates a random blinking effect on the OLED display.
- **Crossfade Animation Demo**: Animates a crossfade effect between two texts on the OLED display.
- **Zoom-in Animation Demo**: Animates a zoom-in effect for a text on the OLED display.
- **Zoom-out Animation Demo**: Animates a zoom-out effect for a text on the OLED display.
- **Jitter Animation Demo**: Simulates a jitter effect for a text on the OLED display.

## Notes

- Adjust animation parameters and texts as needed for customization.
- Ensure that the correct pin numbers are used for SDA and SCL lines based on your hardware setup.
- This code is specifically tailored for MicroPython and may require modifications for other platforms or languages.

