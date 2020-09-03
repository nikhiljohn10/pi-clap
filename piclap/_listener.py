#!/usr/bin/python3
import re
import os
import sys
from time import sleep
import _thread as thread
from array import array
import pyaudio
import statistics as stat

from ._settings import Settings
from ._processor import SignalProcessor


class Listener():
    """Describes methods which are called by user for the initialisation of the PyAudio module to stream microphone input.

    :param config: An object of :class:`Settings` which is used for configuring the module, defaults to None
    :type config: class: :class:`Settings`
    :param bool calibrate: If the flag is set, the chunk size is calibrated, defaults to True
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

    def __init__(self, config=None, calibrate=True):
        """Constructor method"""
        self.config = config or Settings()
        """If the :attr:`config` parameter is ``None``, an object of :class:`Settings` is assigned"""
        self.claps = 0
        """**default:** ``0``

        This class property contains the current count of claps detected"""
        self.lock = thread.allocate_lock()
        self.device = Device(self.config, calibrate)
        """Stores an :class:`Device` object which initialise :obj:`PyAudio` with calibration and manages the audio interface"""
        self.processor = SignalProcessor(method=self.config.method)
        """Initialised with an :class:`SignalProcessor` object using the signal processing method found inside :attr:`config`"""
        print("Algorithm selected:", self.config.method.name)
        # This is to be remove if other algorithms are defineds
        print("Threshold Value:", self.config.method.value)

    def clapWait(self, clap):
        """Start waiting for a small duration of time recursively until no more new claps are detected

        :param int clap: Number of claps found at the time of wait initialised
        """
        sleep(self.config.wait)
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
            self.device.openStream()
            print("Clap detection started")
            while not self.config.exit:
                try:
                    data = self.device.readData()
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
        self.device.closeStream()
        del self.device


class Device:

    def __init__(self, config, calibrate):
        self.config = config
        self.input = pyaudio.PyAudio()
        self.maxSamples = []
        os.system('clear')
        self.__setInputDevice()
        self.__calibrateBufferSize(calibrate)
        print("Default Device:", self.defaultDevice['name'])
        print("Chunk size :", self.config.chunk_size, "bytes")
        print("Rate :", self.config.rate, "Hz")
        print("Channels :", self.config.channels)
        print("Clap wait :", self.config.wait, "sec")
        #sys.exit(0)

    def __del__(self):
        self.input.terminate()

    def __setInputDevice(self):
        if self.input.get_host_api_count() < 1:
            print("No supported PortAudio Host APIs are found in your system")
            sys.exit(1)
        if self.input.get_device_count() < 1:
            print("No input audio device is found in your system")
            sys.exit(1)
        self.defaultDevice = self.input.get_default_input_device_info()
        self.config.channels = int(self.defaultDevice['maxInputChannels'])
        self.config.rate = int(self.defaultDevice['defaultSampleRate'])

    def readData(self):
        return self.stream.read(self.config.chunk_size)

    def openStream(self):
        self.stream = self.input.open(format=pyaudio.paInt16,
                                      channels=self.config.channels,
                                      rate=self.config.rate,
                                      input=True,
                                      frames_per_buffer=self.config.chunk_size)

    def closeStream(self):
        self.stream.stop_stream()
        self.stream.close()

    def __calibrateBufferSize(self, enabled):
        if enabled:
            print(f'\rCalibrating...', end="\r")
            newChunkSize = self.config.chunk_size
            calibrated = False
            totalSamples = 400
            while not calibrated:
                try:
                    self.openStream()
                    for count in range(totalSamples):
                        data = self.stream.read(newChunkSize)
                        byte_stream = array('b', [0]) if data == None else data
                        maximum = max(array('h', byte_stream))
                        self.maxSamples.append(maximum)
                        os.system('clear')
                        self.__printProgress(count, totalSamples)
                    calibrated = True
                except(OSError):
                    if re.search(r'.+Input overflowed$', str(e)):
                        newChunkSize = int(newChunkSize / 2)
            self.closeStream()
            os.system('clear')
            self.config.chunk_size = newChunkSize
            self.setThreshold()
            print("Calibration complete\n")

    def setThreshold(self):
        median = stat.median_high(self.maxSamples)
        value = int(median * 3.141592653589793)
        self.config.method.value = value

    def __printProgress(self, iteration, total):
        terminalSize = re.match("^\D*columns=(\d+), .*$",
                                str(os.get_terminal_size()))
        length = int(int(terminalSize.group(1)) - 24) if terminalSize else 75
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = '█' * filledLength + '_' * (length - filledLength)
        print(f'\rCalibrating: [{bar}] {percent}%', end="\r")
