import os
import sys
from array import array
sys.path.append(os.path.abspath('.'))

from piclap import SignalProcessor
from munch import DefaultMunch as Objectify

DETECTION_ALGORITHMS = [
    'threshold',
    'filter',
    'fft',
    'wavelet'
]

def test_threshold():
    proc = SignalProcessor(method=Objectify.fromDict({
        'name': 'threshold',
        'value': 100
    }, False))
    assert proc.algorithm.name == DETECTION_ALGORITHMS[proc.alg_id], 'Algorithm does not match'
    assert proc.findClap(data=array('b', [99])) == False, 'Clap Detection Error'
    assert proc.findClap(data=array('b', [100])) == False, 'Clap Detection Error'
    assert proc.findClap(data=array('b', [101])) == True, 'Clap Detection Error'
    assert proc.findClap(data=array('b', [102])) == True, 'Clap Detection Error'


if __name__ == '__main__':
    test_threshold()
