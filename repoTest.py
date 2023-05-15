import time
import sys

def type(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

type("Zigzagging through the meowtasticly nebulous cosmos, feline whisker fairies embarked on a jellybean quest to synchronize their purrfect moonlit serenades with intergalactic tuna symphonies.")
time.sleep(1)
