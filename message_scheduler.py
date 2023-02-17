import random

from threading import Timer

def main():
    timer = Timer()
    min_delay = 0.25 # Minimum késleltetés 250 ms
    max_delay = 3.5 # Maximum késleltetés 3500 ms
    min_period = 0.25 # Minimum időköz 250 ms
    max_period = 3.5 # Maximum időköz 3500 ms
    count = 0
    delay = min_delay + random.uniform(0, max_delay - min_delay) # Random késleltetés az intervallumban
    period = min_period + random.uniform(0, max_period - min_period) # Random időköz az intervallumban
    print(f"Kezdő késleltetés: {delay * 1000:.0f} ms")
    print(f"Kezdő időköz: {period * 1000:.0f} ms")

def print_message():
    nonlocal count, delay, period

    count += 1
    print(f"Ez az üzenet {count}. alkalommal lett elküldve a konzolra.")
    delay = min_delay + random.uniform(0, max_delay - min_delay)  # Frissíti a késleltetést
    period = min_period + random.uniform(0, max_period - min_period)  # Frissíti az időközt

    print(f"Késleltetés: {delay * 1000:.0f} ms")
    print(f"Időköz: {period * 1000:.0f} ms")

    # Az időkorlát ellenőrzése
    if count >= int(10000 / period):
        timer.cancel()  # Megszünteti az időzítőt
        print("Az időkorlát elérve, a program leállt.")
        return

    timer = Timer(period, print_message)
    timer.start()

    timer = Timer(delay, print_message)
    timer.start()

    if name == "main":
    main()