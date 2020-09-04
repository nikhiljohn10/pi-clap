
Installation
============

Install Dependencies
-----------------------

Debian/Ubuntu/Rasberry Pi OS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

    # CentOS 8
    sudo dnf upgrade --refresh
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
    python3 -m pip install --user pyaudio || python3 -m pip install --user --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio

Install pi-clap
---------------

Using Git
^^^^^^^^^

.. code-block:: sh

    git clone https://github.com/nikhiljohn10/pi-clap
    cd pi-clap
    make local-install
    make run


``make local-install`` is a helpful tool for alpha/beta testing before deploying to PyPi server


Using Pip
^^^^^^^^^

.. code-block:: sh

    python3 -m pip install --user pi-clap

**Use the module as it is given in the example below.**

Using pi-clap
-------------

Writing an app using pi-clap is only 3 lines it need ideally.

.. literalinclude:: ../../example/app.py
   :language: python
   :linenos:

But this is not the real world senario. You will need more control over the settings that match your microphone and operating system. Following code give your more flexibility.

.. literalinclude:: ../../example/advanced.app.py
   :language: python
   :emphasize-lines: 6-23,26-28,32-33
   :linenos:
