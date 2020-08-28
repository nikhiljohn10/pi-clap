import os
import sys
from array import array
sys.path.append(os.path.abspath('.'))

from piclap import Listener

def test_input():
    input = Listener()
    input.claps = 3
    input.listenClaps("Test")
    assert input.claps == 0, 'listenClaps method did not execute'

if __name__ == '__main__':
    test_input()
