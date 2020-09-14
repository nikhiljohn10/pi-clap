#!/usr/bin/python3

from piclap import *
from gpiozero import LED


class PiController:
    '''Describes the controller methods which are usually used while connected
    to a raspberry pi controller using the module `gpiozero`.
    '''

    def __init__(self):
        self.led12 = LED(12)
        self.led24 = LED(24)

    def toggleLight(self):
        self.led12.toggle()
        print("Light toggled on pin 12")

    def lightBlinker(self, times=10):
        self.led24.blink(n=times)
        print("Light blinks", times, "times on pin 24")


class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        super().__init__()
        self.controller = PiController()
        self.chunk_size = 512       # Reduce as power of 2 if pyaudio overflow
        self.wait = 0.5             # Adjust wait between claps
        self.method.value = 600   # Threshold value adjustment

    def on2Claps(self):
        '''Custom action for 2 claps'''
        self.controller.led12.blink(n=1)
        print("Light flashed on pin 4")

    def on3Claps(self):
        '''Custom action from PiController for 3 claps'''
        self.controller.toggleLight()

    def on5Claps(self):
        '''Custom action from PiController for 5 claps'''
        self.controller.lightBlinker(times=5)


def main():
    config = Config()
    listener = Listener(config)
    listener.start()


if __name__ == '__main__':
    main()
