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

from array import array

DETECTION_METHODS = [           # Method list for clap detection
    'threshold',
    'filter',
    'fft',
    'wavelet'
]


class SignalProcessor():
    def __init__(self, method):
        self.method_id = DETECTION_METHODS.index(method.name)
        self.method = method

    def findClap(self, data):
        if self.method_id == 1:
            return self.useFiter(data)
        elif self.method_id == 2:
            return self.useFFT(data)
        elif self.method_id == 3:
            return self.useWavelets(data)
        else:
            return self.useThreshold(data)

    def useFiter(self, data):
        # TODO
        return False

    def useFFT(self, data):
        # TODO
        return False

    def useWavelets(self, data):
        # TODO
        return False

    def useThreshold(self, data):
        return (True if max(array('h', data)) > self.method.value else False)
