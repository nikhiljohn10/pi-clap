pi-clap
=======

[![Python package](https://github.com/nikhiljohn10/pi-clap/workflows/Python%20package/badge.svg?branch=master)](https://pypi.python.org/pypi/pi-clap/)
[![Latest Version](https://img.shields.io/pypi/v/pi-clap)](https://pypi.python.org/pypi/pi-clap/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pi-clap)](https://pypi.python.org/pypi/pi-clap/)
[![Code Size](https://img.shields.io/github/languages/code-size/nikhiljohn10/pi-clap)](https://pypi.python.org/pypi/pi-clap/)
[![Downloads](https://img.shields.io/pypi/dm/pi-clap)](https://pypi.python.org/pypi/pi-clap/)
[![License](https://img.shields.io/pypi/l/pi-clap)](https://github.com/nikhiljohn10/pi-clap/blob/master/LICENSE)

A python package for clap detection

Visit Official documentation at [pi-clap.nikz.in](https://pi-clap.nikz.in/)

### Platforms Supported

* Raspberry Pi
* Linux
* MacOS

### Hardware Requirements

* Raspberry Pi (optional)
* Bread Board (optional)
* Microphone
* Audio Card (Needed for analog microphones with a jack)

### Dependencies

* [Python 3.6+](https://docs.python.org/3/)
* [gpiozero](https://gpiozero.readthedocs.io)
	* [RPi.GPIO](https://pypi.org/project/RPi.GPIO)
* [PyAudio](https://pypi.org/project/PyAudio)
	* [PortAudio](http://www.portaudio.com/) (Need to be installed manually)
	* Audio Driver (Automatically loaded by OS after a restart)
* [Munch](https://pypi.org/project/munch/)

### Upcoming features

* Adding advanced clap detection algorithms
* Adding support for automation platforms like Amazon Alexa, Google Home, IFTTT etc.

### Development

```
git clone https://github.com/nikhiljohn10/pi-clap
cd pi-clap
make help # Display the possible options available
```

Version number is fetched from [`piclap/__init__.py`](https://github.com/nikhiljohn10/pi-clap/blob/master/piclap/__init__.py)

- Package - [/piclap](https://github.com/nikhiljohn10/pi-clap/tree/master/piclap)
- Examples - [/example](https://github.com/nikhiljohn10/pi-clap/tree/master/example)
- Documentation - [/docs/source](https://github.com/nikhiljohn10/pi-clap/tree/master/docs/source)
- Test Cases - [/test](https://github.com/nikhiljohn10/pi-clap/tree/master/tests)
- Github Actions - [/.github/workflows](https://github.com/nikhiljohn10/pi-clap/tree/master/.github/workflows)

### License

[MIT License](https://github.com/nikhiljohn10/pi-clap/blob/master/LICENSE)
