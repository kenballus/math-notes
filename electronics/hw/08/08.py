# Ben Kallus
# Lights some LEDs in a rising and falling pattern.

from board import *
from digitalio import DigitalInOut, Direction
from time import monotonic

PINS = [D4, D5, D6, SDA, SCL, D9, D10, D11, D12, D13]

def set_state(state, pins):
    start_time = monotonic()

    for pin in pins:
        pin.value = pin < state

    while monotonic() < start_time + (1 if state == 10 else .25):
        pass

def main():
    pins = [DigitalInOut(pin) for pin in PINS]
    for pin in pins:
        pin.direction = Direction.OUTPUT

    state = 0
    direction = 1
    while True:
        state += direction
        set_state(state, pins)
        if state % 10 == 0:
            direction = -direction

main()
