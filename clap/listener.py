#!/usr/bin/python3
from time import sleep

import _thread as thread
import pyaudio
from .processor import SignalProcessor
from .controller import Controller

FORMAT = pyaudio.paInt16		# Signed 16-bit Integer Format
CHANNELS = 1					# 1 = Mono Channel
RATE = 44100					# Number of sample collected in 1 second
CHUNK_SIZE = 1024				# Number of frames in the buffer


class Listener():
    def __init__(self):
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
        self.processor = SignalProcessor()
        # self.rpi = Controller(pin=24)

    def clapWait(self, clap):
        sleep(0.5)
        if self.claps > clap:
            self.clapWait(self.claps)

    def listenClaps(self, threadName):
        with self.lock:
            print("Listener started")
            self.clapWait(self.claps)
            print(self.claps)
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
            print("Clap detection started")
            while not self.exit:
                data = self.stream.read(CHUNK_SIZE)
                if self.processor.findClap(data):
                    self.claps += 1
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
