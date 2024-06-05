import network
import time
import urequests as requests
import ujson as json
import uos as os
import machine

FACTS_FILE = 'facts.json'
MAX_SIZE = 500 * 1024  # 500 KB
THRESHOLD = 0.97 * MAX_SIZE
LED_PIN = 2  # Pin for the LED

# Initialize LED pin
led = machine.Pin(LED_PIN, machine.Pin.OUT)

def connect_wifi(ssid, password):
    """Connect to WiFi."""
    wlan = network.WLAN(network.STA_IF)  # Create WLAN object
    wlan.active(True)  # Activate the WLAN interface
    wlan.connect(ssid, password)  # Connect to WiFi network
    while not wlan.isconnected():  # Wait for connection
        pass
    print("Connected to WiFi")

def is_connected_to_internet():
    """Checks internet connectivity by pinging a public DNS server."""
    try:
        response = requests.get("https://8.8.8.8", timeout=3)  # Ping Google DNS with timeout
        response.close()
        return True
    except:
        return False

def get_random_fact(use_online=True):
    if use_online:
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            fact_text = data["text"]
            fact_details = {
                "id": data["id"],
                "text": data["text"]
            }
            response.close()
            return fact_text, fact_details
        else:
            response.close()
            return None, None
    else:
        # Retrieve a random fact from the JSON file
        if FACTS_FILE in os.listdir():
            with open(FACTS_FILE, 'r') as f:
                facts = json.load(f)
            if facts:
                import random
                random_fact = random.choice(facts)
                return random_fact['text'], random_fact
        return None, None  # Return only text if available

def save_fact(fact_details):
    # Load existing facts
    if FACTS_FILE in os.listdir():
        with open(FACTS_FILE, 'r') as f:
            facts = json.load(f)
    else:
        facts = []

    # Check if the fact already exists
    if any(fact['id'] == fact_details['id'] for fact in facts):
        return

    # Add new fact
    facts.append(fact_details)

    # Check file size and remove oldest facts if necessary
    while len(json.dumps(facts)) > MAX_SIZE:
        facts.pop(0)  # Remove oldest fact

    # Save updated facts
    with open(FACTS_FILE, 'w') as f:
        json.dump(facts, f)

# Connect to WiFi
ssid = "your_ssid"
password = "ssid_pass"
connect_wifi(ssid, password)

while True:
    if is_connected_to_internet():
        fact_text, fact_details = get_random_fact()
    else:
        fact_text, fact_details = get_random_fact(use_online=False)
    
    # Blink LED
    led.value(1)  # Turn on LED
    time.sleep(0.5)  # Wait for 0.5 seconds
    led.value(0)  # Turn off LEDtime.sleep(7)  # Wait before fetching the next fact
    
    if fact_text and fact_details:
        print("Random Fact Text:")
        print(fact_text)
        save_fact(fact_details)
    elif fact_text:
        print("Random Fact Text (Offline):")
        print(fact_text)
    else:
        print("No fact retrieved.")
    
    time.sleep(7)  # Wait before fetching the next fact

