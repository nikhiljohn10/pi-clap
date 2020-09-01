.. highlight::  python

Welcome to Pi Clap
==================

**A python package for clap detection**

Contents
^^^^^^^^

.. toctree::
  :maxdepth: 5
  :caption: Contents
  :hidden:

  Home <self>

.. toctree::

  getting-started
  piclap
  rpi

.. toctree::
  :caption: Links
  :hidden:

  Tutorial <https://magpi.raspberrypi.org/articles/raspberry-pi-clapper>
  Python Package <https://pypi.org/project/pi-clap/>
  Source Code <https://github.com/nikhiljohn10/pi-clap>
  genindex


Platforms Supported
^^^^^^^^^^^^^^^^^^^^

* Raspberry Pi
* Linux
* MacOS


Hardware Requirements
^^^^^^^^^^^^^^^^^^^^^

* Raspberry Pi (optional)
* Bread Board (optional)
* Microphone
* Audio Card (Needed for analog microphones with a jack)

Dependencies
^^^^^^^^^^^^

* `Python 3.6+ <https://docs.python.org/3/>`_
* `PortAudio <http://www.portaudio.com/>`_ (Need to be installed manually)
* `gpiozero <https://gpiozero.readthedocs.io>`_
* `PyAudio <https://pypi.org/project/PyAudio>`_
* `Munch <https://pypi.org/project/munch/>`_
* Audio Driver (Automatically loaded by OS after a restart)

Upcoming features
^^^^^^^^^^^^^^^^^

* Adding advanced clap detection algorithms
* Adding support for automation platforms like Amazon Alexa, Google Home, IFTTT etc.
* Adding auto calibration for microphone

License
^^^^^^^

.. include:: license.rst