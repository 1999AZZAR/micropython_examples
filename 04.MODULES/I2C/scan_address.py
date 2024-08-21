from machine import Pin, I2C
import time

# Define the pins for I2C (change these pins based on your ESP32 setup)
i2c_sda = Pin(21)  # SDA pin
i2c_scl = Pin(22)  # SCL pin

# Initialize I2C bus
i2c = I2C(scl=i2c_scl, sda=i2c_sda)

# Function to perform I2C scan
def i2c_scan():
    devices = i2c.scan()
    if devices:
        print("I2C devices found:")
        for device in devices:
            print("Decimal address: {}, Hex address: 0x{:02x}".format(device, device))
    else:
        print("No I2C devices found.")

# Perform I2C scan
i2c_scan()
