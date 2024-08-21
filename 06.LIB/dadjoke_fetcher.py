import urequests as requests
import json
import os
import machine
import time
import random
from lib.blinker import Blinker

PATH = "dadjokes.json"
MAX_SIZE = 20 * 1024
blinker = Blinker(2)

class DadJokeFetcher:
    def __init__(self):
        self.filepath = PATH

    def get_random_dadjoke(self):
        url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                joke_text = data["joke"]
                joke_details = {
                    "id": data["id"],
                    "joke": data["joke"]
                }
                return joke_text, joke_details
        except:
            pass
        return None, None

    def save_joke_details(self, joke_details):
        try:
            with open(self.filepath, "r") as f:
                jokes = json.load(f)
        except OSError:
            jokes = []

        joke_ids = [joke["id"] for joke in jokes]
        if joke_details["id"] not in joke_ids:
            jokes.append(joke_details)

            while len(json.dumps(jokes)) > MAX_SIZE:
                jokes.pop(0)

            with open(self.filepath, "w") as f:
                json.dump(jokes, f)

    def get_local_joke(self):
        try:
            with open(self.filepath, "r") as f:
                jokes = json.load(f)
            if jokes:
                joke_details = random.choice(jokes)
                return joke_details["joke"], joke_details
        except OSError:
            return None, None

    def get_joke(self):
        joke_text, joke_details = self.get_random_dadjoke()
        if joke_text and joke_details:
            blinker.blink(1, 0.15, 0.15)
            print("Random Dad Joke (on) :")
            print(joke_text)
            self.save_joke_details(joke_details)
        else:
            joke_text, joke_details = self.get_local_joke()
            if joke_text and joke_details:
                blinker.blink(1, 0.2, 0.2)
                print("Random Dad Joke (off) :")
                print(joke_text)
            else:
                blinker.blink(1, 0.25, 0.25)
                print("No jokes available offline.")

