#!/usr/bin/python3
__ENABLED__ = True
try:
    import RPi.GPIO as GPIO
except(ModuleNotFoundError):
    __ENABLED__ = False
    print("Raspberry Pi GPIO module not installed")


class Controller():

    def __init__(self, pin=24):
        if __ENABLED__:
            self.pin = pin
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.pin, GPIO.OUT)

    def flashLight(self, pin=None):
        if __ENABLED__:
            gpio_pin = pin if pin != None else self.pin
            GPIO.output(gpio_pin, True)
            sleep(1)
            GPIO.output(gpio_pin, False)
            print("Light flashed")

    def toggleLight(self, pin=None):
        if __ENABLED__:
            gpio_pin = pin if pin != None else self.pin
            GPIO.output(gpio_pin, not GPIO.input(gpio_pin))
            print("Light toggled")

    def cleanup(self):
        if __ENABLED__:
            GPIO.cleanup()
