#!/usr/bin/python3
"""A pypi demonstration vehicle.

.. module:: pi-clap
   :platform: All
   :synopsis: A clap detection python module

.. moduleauthor:: Nikhil John <ceo@jwala.diamonds>

"""
from time import sleep
import _thread as thread
import pyaudio

from piclap.settings import Settings
from piclap.processor import SignalProcessor


class Listener():
    '''Describes methods which are called by user for the initialisation of the PyAudio module to stream microphone input.

    :param config: An object of :class:`piclap.settings.Settings` which is used for configuring the module
    :type config: class: `piclap.settings.Settings`
    '''
    def __init__(self, config=None):
        self.config = config or Settings()
        self.input = pyaudio.PyAudio()
        self.stream = self.input.open(format=pyaudio.paInt16,
                                      channels=self.config.channels,
                                      rate=self.config.rate,
                                      input=True,
                                      output=True,
                                      frames_per_buffer=self.config.chunk_size)
        self.claps = 0
        self.lock = thread.allocate_lock()
        self.processor = SignalProcessor(method=self.config.method)

    def clapWait(self, clap):
        sleep(self.config.interval)
        if self.claps > clap:
            self.clapWait(self.claps)

    def listenClaps(self, threadName):
        with self.lock:
            print("Waiting for claps...")
            self.clapWait(self.claps)
            action = 'on'+str(self.claps)+'Claps'
            if action in self.config.actions:
                getattr(self.config, action)()
            print("You clapped", self.claps, "times.\n")
            self.claps = 0

    def start(self):
        try:
            print("Clap detection started")
            while not self.config.exit:
                data = self.stream.read(self.config.chunk_size)
                if self.processor.findClap(data):
                    self.claps += 1
                if self.claps == 1 and not self.lock.locked():
                    thread.start_new_thread(
                        self.listenClaps, ("ListenClaps",))
        except(KeyboardInterrupt, SystemExit):
            pass
        self.stop()

    def stop(self):
        print("\rExiting")
        self.config.controller.cleanup()
        self.stream.stop_stream()
        self.stream.close()
        self.input.terminate()
