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

import os
import sys
sys.path.append(os.path.abspath('..'))

from piclap.listener import Listener
from piclap.settings import Settings

def main():
    config = Settings()             # Optional
    config.chunk_size = 512         # Reduce as power of 2 if pyaudio overflow
    config.interval = 1             # Adjust interval between claps
    config.customPin = 13           # Custom config variable
    listener = Listener(config)     # 'config' argument is optional
    listener.start()

if __name__ == '__main__':
    main()
