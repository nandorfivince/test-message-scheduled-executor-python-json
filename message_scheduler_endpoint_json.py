import json
import random
import time

import requests

MIN_DELAY = 0.25  # Minimum késleltetés 250 ms
MAX_DELAY = 3.5  # Maximum késleltetés 3500 ms
MIN_PERIOD = 0.25  # Minimum időköz 250 ms
MAX_PERIOD = 3.5  # Maximum időköz 3500 ms
MAX_COUNT = 10000


def send_message(count, delay, period):
    url = "http://example.com/api/message"
    headers = {"Content-Type": "application/json"}
    message = {"count": count, "delay": delay, "period": period}
    json_message = json.dumps(message)
    response = requests.post(url, headers=headers, data=json_message)
    if response.status_code != 200:
        print("Hiba történt a kérés küldésekor:", response.text)
    else:
        print("Az üzenet sikeresen elküldve a szervert.")

    if __name__ == "main":
        count = 0
        delay = MIN_DELAY + random.uniform(0, MAX_DELAY - MIN_DELAY)
        period = MIN_PERIOD + random.uniform(0, MAX_PERIOD - MIN_PERIOD)
        print(f"Kezdő késleltetés: {delay:.2f} s")
        print(f"Kezdő időköz: {period:.2f} s")

        while count < MAX_COUNT:
            time.sleep(delay)
            count += 1
            send_message(count, delay, period)
            delay = MIN_DELAY + random.uniform(0, MAX_DELAY - MIN_DELAY)
            period = MIN_PERIOD + random.uniform(0, MAX_PERIOD - MIN_PERIOD)
            print(f"Késleltetés: {delay:.2f} s")
            print(f"Időköz: {period:.2f} s")

    print("Az időkorlát elérve, a program leállt.")
