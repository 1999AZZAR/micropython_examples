import urequests as requests
import json
import os
import random

class DadJokeFetcher:
    def __init__(self, filepath="dadjokes.json", max_size_kb=400):
        self.filepath = filepath
        self.max_size_kb = max_size_kb

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
            pass  # Handle the case where the request fails
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

            # Manage file size to be under max_size_kb
            while len(json.dumps(jokes)) > self.max_size_kb * 1024:  # max_size_kb KB
                jokes.pop(0)  # Remove the oldest joke

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
            print("Online Random Dad Joke Text:")
            print(joke_text)
            self.save_joke_details(joke_details)
        else:
            joke_text, joke_details = self.get_local_joke()
            if joke_text and joke_details:
                print("Offline Random Dad Joke Text:")
                print(joke_text)
            else:
                print("No jokes available offline.")

