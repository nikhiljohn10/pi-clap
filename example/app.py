#!/usr/bin/python3
"""

    ###################
    ##               ##
    ##    Pi-Clap    ##
    ##               ##
    ###################

Repo: https://github.com/nikhiljohn10/pi-clap
Author: Nikhil John
License: MIT
"""

try:
    import piclap
except(ModuleNotFoundError):
    import os
    import sys
    sys.path.append(os.path.abspath('.'))

# Above code is only needed if piclap module is not installed using pip install

try:
    import RPi.GPIO
    from piclap.controller import Controller
except(ModuleNotFoundError):
    from piclap.controller import DummyController as Controller
    print("Raspberry Pi GPIO module not installed")

# Above code will load Controller module if availabe

from piclap.settings import Settings
from piclap.listener import Listener


class Config(Settings):

    def __init__(self, pi):
        super().__init__()
        self.pi = pi
        self.chunk_size = 512       # Reduce as power of 2 if pyaudio overflow
        self.interval = 1           # Adjust interval between claps
        self.method.value = 10000   # Threshold value adjustment

    def on2Claps(self):
        self.pi.flashLight(pin=5)

    def on3Claps(self):
        self.pi.toggleLight(pin=6)


def main():
    pi = Controller()
    config = Config(pi=pi)
    listener = Listener(config)
    listener.start()
    pi.cleanup()


if __name__ == '__main__':
    main()
