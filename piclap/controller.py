#!/usr/bin/python3

from time import sleep

try:
    import RPi.GPIO as GPIO

    class Controller():

        def __init__(self):
            self.gpio = GPIO
            self.gpio.setmode(self.gpio.BCM)
            self.setPinOut(pin=24)

        def flashLight(self, pin=24):
            self.gpio.output(pin, True)
            sleep(1)
            self.gpio.output(pin, False)
            print("Light flashed on pin", pin)

        def toggleLight(self, pin=24):
            self.gpio.output(pin, not self.gpio.input(pin))
            print("Light toggled on pin", pin)

        def setPinIn(self, pin):
            self.gpio.setup(pin, self.gpio.IN)

        def setPinOut(self, pin):
            self.gpio.setup(pin, self.gpio.OUT)

        def cleanup(self):
            self.gpio.cleanup()

except(ModuleNotFoundError):

    class Controller():

        def __init__(self):
            pass

        def flashLight(self, pin=None):
            if pin != None:
                print("Light flashed on pin", pin)
            else:
                print("Light flashed")

        def toggleLight(self, pin=None):
            if pin != None:
                print("Light toggled on pin", pin)
            else:
                print("Light toggled")

        def cleanup(self):
            pass

    print("Raspberry Pi GPIO module not installed")
