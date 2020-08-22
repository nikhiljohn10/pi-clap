#!/usr/bin/python3

from time import sleep

try:
    import RPi.GPIO as GPIO
except(ModuleNotFoundError):
    pass


class Controller():

    def __init__(self):
        self.gpio = GPIO
        self.gpio.setmode(gpio.BCM)
        self.setPinOut(pin=24)

    def flashLight(self, pin=None):
        gpio_pin = pin if pin != None else self.pin
        self.gpio.output(gpio_pin, True)
        sleep(1)
        self.gpio.output(gpio_pin, False)
        print("Light flashed")

    def toggleLight(self, pin=None):
        gpio_pin = pin if pin != None else self.pin
        self.gpio.output(gpio_pin, not self.gpio.input(gpio_pin))
        print("Light toggled")

    def setPinIn(self, pin):
        self.gpio.setup(pin, self.gpio.IN)
        self.pin = pin

    def setPinOut(self, pin):
        self.gpio.setup(pin, self.gpio.OUT)
        self.pin = pin

    def cleanup(self):
        self.gpio.cleanup()


# This is only used when RPi module is not found in your system
class DummyController():

    def __init__(self, pin=24):
        pass

    def flashLight(self, pin=None):
        print("Light flashed")

    def toggleLight(self, pin=None):
        print("Light toggled")

    def cleanup(self):
        pass
