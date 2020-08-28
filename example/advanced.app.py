#!/usr/bin/python3

from piclap import *


class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        super().__init__()
        self.chunk_size = 512       # Reduce as power of 2 if pyaudio overflow
        self.interval = 0.5         # Adjust interval between claps
        self.method.value = 10000   # Threshold value adjustment

    def on2Claps(self):
        '''Custom action for 2 claps'''
        print("Light flashed on pin 4")

    def on3Claps(self):
        '''Custom action for 3 claps'''
        print("Light toggled on pin 6")


def main():
    config = Config()
    listener = Listener(config)
    listener.start()


if __name__ == '__main__':
    main()
