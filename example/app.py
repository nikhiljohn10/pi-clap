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

from piclap.controller import Controller
from piclap.settings import Settings
from piclap.listener import Listener


class Config(Settings):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.chunk_size = 512       # Reduce as power of 2 if pyaudio overflow
        self.interval = 1           # Adjust interval between claps
        self.method.value = 10000   # Threshold value adjustment

    def on2Claps(self):
        self.controller.flashLight(pin=5)

    def on3Claps(self):
        self.controller.toggleLight(pin=6)

def main():
    controller = Controller()
    config = Config(controller=controller)
    listener = Listener(config)
    listener.start()
    controller.cleanup()


if __name__ == '__main__':
    main()
