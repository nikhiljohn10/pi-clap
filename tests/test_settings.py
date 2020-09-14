import os
import sys
sys.path.append(os.path.abspath('.'))

from pytest import approx
from piclap import Settings

def test_updating():
    old_config = Settings()
    new_config = Settings()
    new_config.chunk_size = 512
    new_config.wait = 3.5
    new_config.method.value = 300

    assert new_config.chunk_size != old_config.chunk_size, 'Chunk Size not changed'
    assert new_config.wait != approx(old_config.wait), 'Interval not changed'
    assert new_config.method.value != old_config.method.value, 'Threshold value not changed'

if __name__ == '__main__':
    test_updating()
