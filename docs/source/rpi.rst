Raspberry Pi Tutorial
=====================

Hardware Requirements
---------------------

 * Raspberry Pi
 * Microphone
 * Audio Card (Not needed if microphone is connected via USB)
 * Bread Board
 * LED x 2
 * 100 ohm Resistor x 2
 * Jumper wires

 .. image:: _static/pi_circuit.png
   :width: 600
   :alt: Raspberry Pi Circuit

Dependencies
------------


**Python 3**

 * gpiozero
 * PyAudio (PortAudio is needed)
 * Munch

**Other**

 * Rasbian OS
 * Audio Driver

Setting up Raspberry Pi
-----------------------

1. [Download Raspbian OS](http://www.raspberrypi.org/downloads/)
2. Install Raspbian OS in RPi [4]
3. Plugin the USB input audio device(Audio Card or Microphone)
4. Configure OS after OS bootup [6] `sudo raspi-config`
5. Update OS `sudo apt-get update && sudo apt-get upgrade -y`
6. Reboot `sudo reboot` (This should enable the audio driver for the device connected)
7. Install pip & portaudio module `sudo apt-get install -y python3-pip portaudio19-dev`
8. Install pi-clap pip module `pip3 install pi-clap`
9. Connect the output line to BCM #4 & #6 Pin on Raspberry Pi.

( Try 2 claps to activate the output line for 1 sec and 3 claps to toggle ON/OFF state of given PIN. Note: Use 4 claps to exit from the system )
