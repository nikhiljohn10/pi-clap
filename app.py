#!/usr/bin/python3
"""

	###################
	##               ##
	##    Pi-Clap    ##
	##               ##
	###################

Repo: https://github.com/nikhiljohn10/pi-clap
Author: Nikhil John

"""
import _thread as thread
from array import array
from time import sleep
import pyaudio
# import RPi.GPIO as GPIO

FORMAT = pyaudio.paInt16	# Signed 16-bit Integer Format
CHANNELS = 1				# 1 = Mono (Supported), 2 = Stereo (Stereo is not supported yet)
RATE = 44100				# Number of sample collected in 1 second
CHUNK_SIZE = 1024			# Number of frames in the buffer
LISTENER_WAIT = 2 			# Adjsut wait time for listener
LISTENER_THRESHOLD = 10000  # Adjust threshold amplitude

# class Controller():
#
# 	def __init__(self, pin):
# 		self.pin = pin
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(self.pin, GPIO.OUT)
#
# 	def flashLight(pin=None):
# 	 	gpio_pin = pin if pin != None else self.pin
# 		GPIO.output(gpio_pin,True)
# 		sleep(1)
# 		GPIO.output(gpio_pin,False)
# 		print("Light flashed")
#
# 	def toggleLight(pin=None):
# 	 	gpio_pin = pin if pin != None else self.pin
# 		GPIO.output(gpio_pin, not GPIO.input(gpio_pin))
# 		print("Light toggled")
#
# 	def cleanup():
# 		GPIO.cleanup()

class Listener():
    def __init__(self):
        self.threshold = LISTENER_THRESHOLD
        self.input = pyaudio.PyAudio()
        self.stream = self.input.open(format=FORMAT,
                                      channels=CHANNELS,
                                      rate=RATE,
                                      input=True,
                                      output=True,
                                      frames_per_buffer=CHUNK_SIZE)
        self.claps = 0
        self.exit = False
        self.lock = thread.allocate_lock()
		# self.rpi = Controller(pin=24)

    def listenClaps(self, threadName):
        with self.lock:
            print("Listener started")
            sleep(LISTENER_WAIT)
            if self.claps == 2:
                print("Clapped 2 times.")
				# self.rpi.flashLight()
            elif self.claps == 3:
                print("Clapped 3 times.")
				# self.rpi.toggleLight(pin=13)
            elif self.claps == 4:
                self.exit = True
            self.claps = 0
            print("Listener stopped")

    def start(self):
        try:
            while not self.exit:
                data = self.stream.read(CHUNK_SIZE)
                as_ints = array('h', data)
                max_value = max(as_ints)
                if max_value > self.threshold:
                    self.claps += 1
                    print("Clapped")
                if self.claps == 1 and not self.lock.locked():
                    thread.start_new_thread(
                        self.listenClaps, ("ListenClaps",))
        except (KeyboardInterrupt, SystemExit):
            pass
        self.stop()

    def stop(self):
        print("\rExiting")
        self.stream.stop_stream()
        self.stream.close()
        self.input.terminate()
        # self.rpi.cleanup()


def main():
    listener = Listener()
    listener.start()


if __name__ == '__main__':
    main()
