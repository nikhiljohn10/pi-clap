import os
import sys
sys.path.append(os.path.abspath('.'))

from piclap.settings import Settings

def getSettings():
    config = Settings()
    config.chunk_size = 512
    config.interval = 1
    config.customPin = 13
    return config

def test():
    old_config = Settings()
    new_config = getSettings()
    assert new_config.chunk_size != old_config.chunk_size, 'Chunk Size not changed'
    assert new_config.interval != old_config.interval, 'Interval not changed'
    assert new_config.customPin != None, 'Custom Pin not set'

if __name__ == '__main__':
    test()
