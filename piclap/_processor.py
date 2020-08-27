#!/usr/bin/python3

from array import array

DETECTION_METHODS = [           # Method list for clap detection
    'threshold',
    'filter',
    'fft',
    'wavelet'
]


class SignalProcessor():
    """Describes all the signal processing algorithms and selector method.

    :param method: An object that contain the configuration and details of which method to be used for processing the data received.
    :type method: class: `Munch`
    :var int method_id: Stores the ID of the method used
    :var method: Stores the configuration of the method used
    :vartype method: class: `Munch`
    """

    def __init__(self, method):
        self.method_id = DETECTION_METHODS.index(method.name)
        """**default:** ``0``
        
        Search for the method name in the ``DETECTION_METHODS`` and Store the id found
        """
        self.method = method
        """The method stored in this variable is used throughout the execution"""

    def findClap(self, data):
        """Based on the detection method selected, the data given to the selected algorithm
        
        :param data: Binary data received from microphone
        :type data: bytearray
        :return: `True` if clap is detected, `False` otherwise
        :rtype: bool
        """
        byte_stream = array('b', [0]) if data == None else data
        if self.method_id == 1:
            return self.useFiter(byte_stream)
        elif self.method_id == 2:
            return self.useFFT(byte_stream)
        elif self.method_id == 3:
            return self.useWavelets(byte_stream)
        else:
            return self.useThreshold(byte_stream)

    def useFiter(self, byte_stream):
        # TODO
        return False

    def useFFT(self, byte_stream):
        # TODO
        return False

    def useWavelets(self, byte_stream):
        # TODO
        return False

    def useThreshold(self, byte_stream):
        return (True if max(array('h', byte_stream)) > self.method.value else False)
