# MicroPython Analog Input Examples

This directory contains MicroPython examples related to reading analog inputs.

## Contents

- ADC - Read analog voltage on an ADC pin
- Smoothing - Read analog value with smoothing

## Requirements

- MicroPython board
- Analog sensor like potentiometer
- Jumper wires
- Breadboard

## Usage

These examples demonstrate:

- Reading raw analog values (0-4095 range)
- Converting value to a voltage based on ADC reference voltage
- Smoothing readings using a running average

### To run

- Connect analog sensor to ADC input pin
- Modify pin number as needed
- Upload code and view serial output
- Rotate potentiometer to see changing values

### *Notes*

- ADC pins vary across boards - use a labeled ADC/analog pin
- Adjust voltage conversion for different ADC refs

## Contributing

Contributions welcome! Please open an issue or PR for any bugs or improvements.
