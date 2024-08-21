import urequests as requests
import json
import os
import machine
import time
import random
from lib.blinker import Blinker

PATH = "facts.json"
MAX_SIZE = 20 * 1024
blinker = Blinker(2)

class FactsFetcher:
    def __init__(self):
        self.filepath = PATH

    def get_random_fact(self):
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                fact_text = data["text"]
                fact_details = {
                    "id": data["id"],
                    "fact": data["text"]
                }
                return fact_text, fact_details
        except:
            pass
        return None, None

    def save_fact_details(self, fact_details):
        try:
            with open(self.filepath, "r") as f:
                facts = json.load(f)
        except OSError:
            facts = []

        fact_ids = [fact["id"] for fact in facts]
        if fact_details["id"] not in fact_ids:
            facts.append(fact_details)

            while len(json.dumps(facts)) > MAX_SIZE:
                facts.pop(0)

            with open(self.filepath, "w") as f:
                json.dump(facts, f)

    def get_local_fact(self):
        try:
            with open(self.filepath, "r") as f:
                facts = json.load(f)
            if facts:
                fact_details = random.choice(facts)
                return fact_details["fact"], fact_details
        except OSError:
            return None, None

    def get_fact(self):
        fact_text, fact_details = self.get_random_fact()
        if fact_text and fact_details:
            blinker.blink(1, 0.15, 0.15)
            print("Random fact (on) :")
            print(fact_text)
            self.save_fact_details(fact_details)
        else:
            fact_text, fact_details = self.get_local_fact()
            if fact_text and fact_details:
                blinker.blink(1, 0.2, 0.2)
                print("Random fact (off) :")
                print(fact_text)
            else:
                blinker.blink(1, 0.25, 0.25)
                print("No facts available offline.")

