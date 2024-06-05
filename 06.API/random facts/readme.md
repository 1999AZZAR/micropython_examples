# Random Fact Retriever

## Description

This MicroPython code is designed to run on ESP32 devices and retrieves random useless facts from an online API (https://uselessfacts.jsph.pl/api/v2/facts/random). It can also store a limited number of retrieved facts locally in a JSON file and retrieve them offline when no internet connection is available. The code utilizes an LED to provide visual feedback when a new fact is retrieved, blinking the LED for a short duration.

## How It Works

1. **Importing Modules and Defining Constants**
   - The code begins by importing necessary modules: `network` for WiFi connectivity, `time` for time-related operations, `urequests` for making HTTP requests, `ujson` for working with JSON data, `uos` for interacting with the operating system, and `machine` for controlling hardware components.
   - Constants are defined for the filename to store facts (`FACTS_FILE`), the maximum file size for storing facts (`MAX_SIZE`), a threshold for triggering file size management (`THRESHOLD`), and the LED pin number (`LED_PIN`).

2. **Initializing LED**
   - The LED pin is initialized using the `machine.Pin` class, setting it as an output pin.

3. **WiFi Connection**
   - The `connect_wifi` function is responsible for connecting the device to a WiFi network using the provided SSID and password.
   - It creates a WLAN object, activates the WLAN interface, and attempts to connect to the specified WiFi network.
   - The function waits until a successful connection is established before continuing.

4. **Internet Connectivity Check**
   - The `is_connected_to_internet` function checks if the device has an active internet connection by pinging a public DNS server (8.8.8.8) using a GET request with a timeout of 3 seconds.
   - If the request is successful, the function returns `True`, indicating an active internet connection. Otherwise, it returns `False`.

5. **Random Fact Retrieval**
   - The `get_random_fact` function is responsible for retrieving a random fact.
   - If an internet connection is available (`use_online=True`), it sends a GET request to the online API and retrieves a random fact in JSON format.
   - If the response is successful (status code 200), the function extracts the fact text and details (ID and text) from the JSON data and returns them.
   - If an internet connection is not available (`use_online=False`), the function attempts to retrieve a random fact from the locally stored JSON file (`FACTS_FILE`).
   - If the JSON file exists and contains facts, a random fact is selected and returned.
   - If no fact is available, the function returns `None` for both the fact text and details.

6. **Fact Saving**
   - The `save_fact` function saves a new fact to the local JSON file (`FACTS_FILE`).
   - It first loads any existing facts from the JSON file.
   - If the new fact already exists (based on the fact ID), the function returns without saving the fact.
   - Otherwise, the new fact is appended to the list of existing facts.
   - To manage the file size, the function checks if the JSON representation of the updated facts exceeds the `MAX_SIZE`. If so, it removes the oldest facts until the size is below the specified threshold (`THRESHOLD`).
   - Finally, the updated list of facts is saved to the JSON file.

7. **Main Program Loop**
   - The code connects to the WiFi network using the provided SSID and password.
   - Inside an infinite loop, the program performs the following steps:
     - Checks if an internet connection is available using the `is_connected_to_internet` function.
     - Retrieves a random fact using the `get_random_fact` function, passing `use_online=True` if an internet connection is available, or `use_online=False` if not.
     - Blinks the LED by turning it on for 0.5 seconds and then off, providing visual feedback that a new fact has been retrieved.
     - If a fact text and details were successfully retrieved, the fact text is printed to the console, and the fact details are saved to the local JSON file using the `save_fact` function.
     - If only the fact text was retrieved (offline mode), it is printed to the console with an indication that it was retrieved offline.
     - If no fact was retrieved, a message is printed indicating that no fact was retrieved.
     - The program waits for 7 seconds before repeating the loop and fetching the next fact.

## Structure

The code is structured into several functions:

- `connect_wifi(ssid, password)`: Connects the device to a WiFi network.
- `is_connected_to_internet()`: Checks if the device has an active internet connection.
- `get_random_fact(use_online=True)`: Retrieves a random fact from the online API or the local JSON file.
- `save_fact(fact_details)`: Saves a new fact to the local JSON file, managing the file size.

The main program flow is contained in the loop at the end of the code, which connects to WiFi, retrieves a random fact, blinks the LED, prints the fact, saves the fact (if retrieved online), and waits before repeating the process.

## Notes

- This code was written and tested on ESP32 devices using MicroPython.
- The code assumes that the WiFi SSID and password are provided as variables (`ssid` and `password`).
- The maximum file size for storing facts is set to 500 KB, and a threshold of 97% is used to trigger file size management.
- The LED pin number is set to 2, but it can be changed if necessary.
- The code uses the `urequests` module for making HTTP requests and the `ujson` module for working with JSON data, which are optimized for use in MicroPython.
- Error handling is minimal in this code, and it assumes that the API and JSON file operations are successful.
