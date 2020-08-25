Getting Started
===============

Dependencies
------------

Debian/Ubuntu/Rasbian OS
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    sudo apt-get update && sudo apt-get upgrade -y
    sudo apt-get install -y python3-pip portaudio19-dev

Fedora
^^^^^^

.. code-block:: sh

    sudo dnf upgrade --refresh
    sudo dnf install -y python3-pip portaudio-devel redhat-rpm-config

Centos
^^^^^^

.. code-block:: sh

    # CentOS 8s
    udo dnf upgrade --refresh
    sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

    # CentOS 7
    yum -y update
    rpm -Uvh https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-11.noarch.rpm

    # CentOS 6
    yum -y update
    rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

    sudo yum install -y python37-pip portaudio portaudio-devel

MacOS
^^^^^

.. code-block:: sh

    brew install python3 portaudio
    pip3 install pyaudio munch || pip3 install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio munch

Installation
------------

Using Pip package
^^^^^^^^^^^^^^^^^

.. code-block:: sh

    pip3 install pi-clap

Using Git Clone
^^^^^^^^^^^^^^^

.. code-block:: sh

    git clone https://github.com/nikhiljohn10/pi-clap
    cd pi-clap
    make run

Example code
------------

.. code-block::

    from piclap import Listener, Settings


    class Config(Settings):
    	'''This is an user defined derived class with `piclap.Settings` as base class'''

        def __init__(self):
            '''Defines new and override existing properties here'''
            super().__init__()
            self.chunk_size = 512       # Reduce as power of 2 if pyaudio overflow
            self.interval = 1.0         # Adjust interval between claps
            self.method.value = 300		# Threshold value adjustment

        def on2Claps(self):
            '''Custom action for 2 claps'''
            self.controller.flashLight(pin=4)

        def on3Claps(self):
            '''Custom action for 3 claps'''
            self.controller.toggleLight(pin=6)

    config = Config()
    listener = Listener(config)
    listener.start()
