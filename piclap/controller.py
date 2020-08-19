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
from time import sleep

try:
    import RPi.GPIO as GPIO
except(ModuleNotFoundError):
    pass


class Controller():

    def __init__(self, pin=24):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def flashLight(self, pin=None):
        gpio_pin = pin if pin != None else self.pin
        GPIO.output(gpio_pin, True)
        sleep(1)
        GPIO.output(gpio_pin, False)
        print("Light flashed")

    def toggleLight(self, pin=None):
        gpio_pin = pin if pin != None else self.pin
        GPIO.output(gpio_pin, not GPIO.input(gpio_pin))
        print("Light toggled")

    def cleanup(self):
        GPIO.cleanup()


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
