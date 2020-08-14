#!/usr/bin/python3

from array import array

THRESHOLD = 10000               # Adjust threshold amplitude
DETECTION_METHODS = [           # Method list for clap detection
    'threshold',
    'filter',
    'fft',
    'wavelet'
]


class SignalProcessor():
    def __init__(self, method='threshold'):
        self.method_id = DETECTION_METHODS.index(method)

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
        return (True if max(array('h', data)) > THRESHOLD else False)
