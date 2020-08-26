#!/usr/bin/python3
from time import sleep
import _thread as thread
import pyaudio

from ._settings import Settings
from ._processor import SignalProcessor


class Listener():
    """Describes methods which are called by user for the initialisation of the PyAudio module to stream microphone input.

    :param config: An object of :class:`Settings` which is used for configuring the module, defaults to None
    :type config: class: :class:`Settings`
    :var config: Store the `Settings` object
    :vartype config: class: `Settings`
    :var input: Store the `PyAudio` object
    :vartype input: class: `pyaudio.PyAudio`
    :var stream: Open a new input audio stream and store the stream object
    :vartype stream: class: `pyaudio.Stream`
    :var int claps: Store current value of claps counted and initially set to `0`
    :var lock: Store the thread lock
    :vartype lock: thread.lock
    :var processor: Store the `Processor` object
    :vartype processor: class: `SignalProcessor`
    """

    def __init__(self, config=None):
        """Constructor method"""
        self.config = config or Settings()
        """If the :attr:`config` parameter is ``None``, an object of :class:`Settings` is assigned"""
        self.input = pyaudio.PyAudio()
        """Initialised with an :class:`pyaudio.PyAudio` object"""
        self.stream = self.input.open(format=pyaudio.paInt16,
                                      channels=self.config.channels,
                                      rate=self.config.rate,
                                      input=True,
                                      frames_per_buffer=self.config.chunk_size)
        """Initialised with an :class:`pyaudio.Stream` object"""
        self.claps = 0
        """**default:** ``0``

        This class property contains the current count of claps detected"""
        self.lock = thread.allocate_lock()
        self.processor = SignalProcessor(method=self.config.method)
        """Initialised with an :class:`SignalProcessor` object using the signal processing method found inside :attr:`config`"""

    def clapWait(self, clap):
        """Start waiting for an interval of time recursively until no more new claps are detected

        :param int clap: Number of claps found at the time of wait initialised
        """
        sleep(self.config.interval)
        if self.claps > clap:
            self.clapWait(self.claps)

    def listenClaps(self, threadName):
        """This method runs on a child thread with :attr:`lock` when :attr:`claps` equals ``1`` and reset the class property :attr:`claps` to ``0`` when execution is finished

        :param str threadName: Name of the child thread started
        """
        with self.lock:
            print("Waiting for claps...")
            self.clapWait(self.claps)
            action = 'on' + str(self.claps) + 'Claps'
            if action in self.config.actions:
                getattr(self.config, action)()
            print("You clapped", self.claps, "times.\n")
            self.claps = 0

    def start(self):
        """When this method is called, the listener start reading binary data from stream and sreach for claps inside the chunks of data using :class:`SignalProcessor` until :attr:`Settings.exit` flag is ``True``

        :raises: ``KeyboardInterrupt``: If **Control + C** is pressed on keyboard
        """
        try:
            print("Clap detection started")
            while not self.config.exit:
                try:
                    data = self.stream.read(self.config.chunk_size)
                except (OSError, IOError):
                    data = None
                if self.processor.findClap(data):
                    self.claps += 1
                if self.claps == 1 and not self.lock.locked():
                    thread.start_new_thread(
                        self.listenClaps, ("ListenClaps",))
        except(KeyboardInterrupt, SystemExit):
            pass
        self.stop()

    def stop(self):
        """When this method is called, the listener stop listening by closing the stream safely and terminating the connection"""
        print("\rExiting")
        self.stream.stop_stream()
        self.stream.close()
        self.input.terminate()
