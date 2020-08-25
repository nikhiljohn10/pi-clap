#!/usr/bin/python3

from array import array

DETECTION_METHODS = [           # Method list for clap detection
    'threshold',
    'filter',
    'fft',
    'wavelet'
]


class SignalProcessor():
    """

    """
    def __init__(self, method):
        self.method_id = DETECTION_METHODS.index(method.name)
        self.method = method

    def findClap(self, data):
        bit_stream = array('b', [0]) if data == None else data
        if self.method_id == 1:
            return self.useFiter(bit_stream)
        elif self.method_id == 2:
            return self.useFFT(bit_stream)
        elif self.method_id == 3:
            return self.useWavelets(bit_stream)
        else:
            return self.useThreshold(bit_stream)

    def useFiter(self, bit_stream):
        # TODO
        return False

    def useFFT(self, bit_stream):
        # TODO
        return False

    def useWavelets(self, bit_stream):
        # TODO
        return False

    def useThreshold(self, bit_stream):
        return (True if max(array('h', bit_stream)) > self.method.value else False)
