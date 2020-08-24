#!/usr/bin/python3
'''

    ###################
    ##               ##
    ##    Pi-Clap    ##
    ##               ##
    ###################

Repo: https://github.com/nikhiljohn10/pi-clap
Author: Nikhil John
License: MIT
'''

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


class UserController(Controller):
    '''Describes the controller methods which are usually used while connected
    to a raspberry pi controller using the module `RPi.GPIO`. This class is not
    need when used without a Raspberry Pi.

    format:
        class UserController(Controller):

            def __init__(self):
                super().__init__()

            def actionName(self):
                # Add custom action code here
    '''

    def __init__(self):
        super().__init__()

    def lightBlinker(self, pin, times=10):
        '''Following code is only used when code runs on a Raspberry Pi'''
        # setPinOut(pin)
        # for i in range(times):
        #     self.gpio.output(pin, True)
        #     sleep(0.5)
        #     self.gpio.output(pin, False)
        #     sleep(0.5)
        print("Light blinks", times, "times on pin", pin)


class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.

    format:
        class Config(Settings):

            def __init__(self):
                # Only pass UserController() object as parameter if it is needed
                super().__init__(UserController())
                # Add class properties here

            # N is the number of claps to wait for the action to execute
            def on<N>Claps(self):
                # Add controller actions or custom actions
    '''

    def __init__(self):
        super().__init__(UserController())
        self.chunk_size = 512       # Reduce as power of 2 if pyaudio overflow
        self.interval = 1           # Adjust interval between claps
        self.method.value = 10000   # Threshold value adjustment

    def on2Claps(self):
        '''Custom action for 2 claps'''
        self.controller.flashLight(pin=4)

    def on3Claps(self):
        '''Custom action for 3 claps'''
        self.controller.toggleLight(pin=6)

    def on5Claps(self):
        '''Custom action for 5 claps'''
        self.controller.lightBlinker(pin=5, times=5)


def main():
    config = Config()
    listener = Listener(config)
    listener.start()


if __name__ == '__main__':
    main()
