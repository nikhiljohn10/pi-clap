#!/usr/bin/python3
try:
    import RPi.GPIO as GPIO
except(ModuleNotFoundError):
    print("Raspberry Pi GPIO module not installed")


class Controller():

    def __init__(self, pin=24):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def flashLight(pin=None):
        gpio_pin = pin if pin != None else self.pin
        GPIO.output(gpio_pin, True)
        sleep(1)
        GPIO.output(gpio_pin, False)
        print("Light flashed")

    def toggleLight(pin=None):
        gpio_pin = pin if pin != None else self.pin
        GPIO.output(gpio_pin, not GPIO.input(gpio_pin))
        print("Light toggled")

    def cleanup():
        GPIO.cleanup()
