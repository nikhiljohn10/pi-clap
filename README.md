pi-clap
=======

[![Python package](https://github.com/nikhiljohn10/pi-clap/workflows/Python%20package/badge.svg?branch=master)](https://pypi.python.org/pypi/pi-clap/)
[![Latest Version](https://img.shields.io/pypi/v/pi-clap)](https://pypi.python.org/pypi/pi-clap/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pi-clap)](https://pypi.python.org/pypi/pi-clap/)
[![Dependencies](https://img.shields.io/badge/deps-portaudio%2C%20pyaudio%2C%20munch-informational)](https://pypi.python.org/pypi/pi-clap/)
[![Code Size](https://img.shields.io/github/languages/code-size/nikhiljohn10/pi-clap)](https://pypi.python.org/pypi/pi-clap/)
[![Downloads](https://img.shields.io/pypi/dm/pi-clap)](https://pypi.python.org/pypi/pi-clap/)
[![License](https://img.shields.io/pypi/l/pi-clap)](https://github.com/nikhiljohn10/pi-clap/blob/master/LICENSE)

A python package for clap detection

**Platforms Supported:** *Raspberry Pi, Linux, MacOS*

### H/w Requirements

 * Raspberry Pi
 * Microphone [5]
 * Audio Card [5]
 * Bread Board (optional)

### Dependencies

**Python 3**

 * RPi.GPIO
 * pyaudio ( PortAudio is needed )
 * [munch](https://github.com/Infinidat/munch)

**Other**

 * Rasbian OS [3]
 * Audio Driver [1],[2],[3]

### Setting up Raspberry Pi

1. [Download Raspbian OS](http://www.raspberrypi.org/downloads/)
2. [Install Raspbian OS in RPi](http://www.raspberrypi.org/documentation/installation/installing-images/)
3. Plugin the USB input audio device(Audio Card or Microphone)
4. Configure OS after OS bootup [6] `sudo raspi-config`
5. Update OS `sudo apt-get update && sudo apt-get upgrade -y`
6. Reboot `sudo reboot` (This should enable the audio driver for the device connected)
7. Install pip & portaudio module `sudo apt-get install -y python3-pip portaudio19-dev`
8. Install pi-clap pip module `pip3 install pi-clap`
9. Connect the output line to BCM #24 & #13 Pin on RPi.

( Try 2 claps to activate the output line for 1 sec and 3 claps to toggle ON/OFF state of given PIN. Note: Use 4 claps to exit from the system )

### Installing dependencies for other operating systems

```
# Debian based OS like Ubuntu

sudo apt-get install -y python3-pip portaudio19-dev

```

```
# Fedora

sudo dnf install -y python3-pip portaudio-devel redhat-rpm-config
pip3 install --user pyaudio

```

```
# Centos

sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm # CentOS 8
rpm -Uvh https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-11.noarch.rpm # CentOS 7
rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm # CentOS 6

sudo yum install -y python37-pip portaudio portaudio-devel
pip3 install pyaudio
```

```
# MacOS

brew install portaudio
pip3 install pyaudio munch || pip3 install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio munch
```

### Example code

```
# Example code for using the package

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

```

### Using Pip package

```
# Using the following command in terminal
pip3 install pi-clap
```

### Using Git Clone
```
git clone https://github.com/nikhiljohn10/pi-clap
cd pi-clap
python3 tests/app.py
```

### License

[MIT](https://github.com/nikhiljohn10/pi-clap/blob/master/LICENSE)

### References

 1. https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/instructions
 2. http://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876
 3. http://forum.kodi.tv/showthread.php?tid=172072
 4. http://www.raspberrypi.org/documentation/installation/installing-images/
 5. https://raspberrytips.com/add-microphone-raspberry-pi/
 6. https://www.raspberrypi.org/documentation/configuration/
