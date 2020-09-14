#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath('.'))

from piclap import *


class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        Settings.__init__(self)
        self.method.value = 10000

    def on2Claps(self):
        '''Custom action for 2 claps'''
        print("Light flashed on pin 4")

    def on3Claps(self):
        '''Custom action for 3 claps'''
        print("Light toggled on pin 6")


def main():
    config = Config()
    listener = Listener(config=config, calibrate=False)
    listener.start()


if __name__ == '__main__':
    main()
