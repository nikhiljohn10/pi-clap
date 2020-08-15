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

from piclap.listener import Listener


def main():
    listener = Listener()
    listener.start()


if __name__ == '__main__':
    main()
