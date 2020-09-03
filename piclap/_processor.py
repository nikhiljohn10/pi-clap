#!/usr/bin/python3

from array import array

DETECTION_ALGORITHMS = [           # Method list for clap detection
    'threshold',
    'filter',
    'fft',
    'wavelet'
]

class SignalProcessor():
    """Describes all the signal processing algorithms and selector method.

    :param method: An object that contain the configuration and details of which algorithm to be used for processing the data received.
    :type method: class: `Munch`
    :var int alg_id: Stores the ID of the algorithm used
    :var algorithm: Stores the configuration of the algorithm used
    :vartype algorithm: class: `Munch`
    """

    def __init__(self, method):
        self.alg_id = DETECTION_ALGORITHMS.index(method.name)
        """**default:** ``0``

        Search for the algorithm name in the ``DETECTION_ALGORITHMS`` and store the id found
        """
        self.algorithm = method
        """The algorithm stored in this variable is used throughout the execution"""

    def findClap(self, data):
        """Based on the detection algorithm selected, the data is given to the selected algorithm

        :param data: Binary data received from microphone
        :type data: bytearray
        :return: `True` if clap is detected, `False` otherwise
        :rtype: bool
        """
        byte_stream = array('b', [0]) if data == None else data
        if self.alg_id == 1:
            return self.useFiter(byte_stream)
        elif self.alg_id == 2:
            return self.useFFT(byte_stream)
        elif self.alg_id == 3:
            return self.useWavelets(byte_stream)
        else:
            return self.useThreshold(byte_stream)

    def useFiter(self, byte_stream):
        """This algorithm is not implemented yet

        :param byte_stream: Binary stream of data received from microphone
        :type byte_stream: bytearray
        """
        # TODO
        return False

    def useFFT(self, byte_stream):
        """This algorithm is not implemented yet

        :param byte_stream: Binary stream of data received from microphone
        :type byte_stream: bytearray
        """
        # TODO
        return False

    def useWavelets(self, byte_stream):
        """This algorithm is not implemented yet

        :param byte_stream: Binary stream of data received from microphone
        :type byte_stream: bytearray
        """
        # TODO
        return False

    def useThreshold(self, byte_stream):
        """This algorithm uses a threshold value to detect claps.

        :param byte_stream: Binary stream of data received from microphone
        :type byte_stream: bytearray
        :return: When the maximum value of the integer array is greater than threshold, it returns `True` and `False` if otherwise
        :rtype: bool
        """
        max_value = max(array('h', byte_stream))
        return (True if max_value > self.algorithm.value else False)
