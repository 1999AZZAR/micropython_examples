# MicroPython SSD1306 OLED Display Examples

This directory contains MicroPython code for using the SSD1306 OLED display module with I2C interface.

## Contents

- The examples demonstrate:

  - Initializing the display
  - Drawing pixels, lines, rectangles, text
  - Scrolling text
  - Displaying images

## Requirements

- MicroPython board (tested on ESP32)
- SSD1306 OLED display module 128x64 pixels
- I2C connection between board and display
- ssd1306 MicroPython module

## Usage

- Connect display to board using I2C pins (SDA, SCL)
- Modify I2C initialization as needed
- Run the example code to draw graphics, text, images
- View output on the OLED display

### Notes

See particular example code for wiring connections
May need to adjust I2C freq for stability

## Contributing

Contributions welcome! Please open an issue or PR for any bugs or improvements.
