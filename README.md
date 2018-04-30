pi-clap
=======

Clap detection and singnaling program for Raspberry Pi

### H/w Requirements

 * Raspberry Pi
 * Microphone
 * Audio Card
 * Bread Board (optional)

### Dependencies

**Python**

 * RPi.GPIO
 * pyaudio

**Other**

 * Rasbian OS [3].( Need to test. Not working with Pidora OS)
 * Audio Driver [1],[2],[3].

### Setting up

1. [Download Raspbian OS](http://www.raspberrypi.org/downloads/).
2. [Install Raspbian OS in RPi](http://www.raspberrypi.org/documentation/installation/installing-images/).
3. Install all dependecies
4. Connect the output line to BCM #24 Pin on RPi.
5. Run 'sudo python main.py' command in terminal.

( Try 2 claps to activate the output line for 1 sec. Note: Use 4 claps to exit from the system )

### References

 1. https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/instructions
 2. http://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876
 3. http://forum.kodi.tv/showthread.php?tid=172072
 4. http://www.raspberrypi.org/documentation/installation/installing-images/
