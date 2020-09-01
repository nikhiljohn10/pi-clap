Raspberry Pi Tutorial
=====================

Hardware Requirements
---------------------

* Raspberry Pi with OS installed on SD Card x 1
* Microphone x 1
* Audio Card x 1 (Not needed if microphone is connected via USB)
* Bread Board x 1
* LED x 2
* 100 ohm Resistor x 2
* Jumper wires x 5

Dependencies
------------

* Python 3.6+
* gpiozero
* PyAudio (PortAudio is needed)
* Munch

Setting up Raspberry Pi
-----------------------

1. Flash a 8GB+ memory card with Rasberry OS Lite
2. Insert the card in to Raspberry Pi
3. Connect monitor, keyboard, ethernet and power to Raspberry Pi
4. Turn on the power and let the OS bootup
5. Use username: ``pi`` and password: ``raspberry`` to login
6. Use ``sudo raspi-config`` to configure

	* Change password
	* Enable SSH
	* Enable any interface options as needed
	* Expand the filesystem ( Advance optoins > Expand filesystem)
  
7. Update system using ``sudo apt-get update && sudo apt-get upgrade -y``

Now you are updated and ready to use via SSH from different computer. Now you can disconnect monitor and keyboard if you want to use SSH.

Using Pi Clap
-------------

 .. image:: _static/pi_circuit.png
   :width: 600
   :alt: Raspberry Pi Circuit

How to wire up for Pi Clap?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Connect ``Ground Pin(6)`` to breadboard's sideline
2. Connect one Red LED and 100ohm Resistor in serial with LED's positive ends
3. Connect negative ends of LEDs to grounded sideline
4. Connect the Resisters to GPIO 12 & 24 Pins on Raspberry Pi as in the circuit diagram
5. Plugin the USB input audio device(Audio Card or Microphone)
6. Reboot the OS with `sudo reboot` (This should load the audio driver automatically in most cases for the device connected)
7. Install pip & portaudio module ``sudo apt-get install -y python3-pip portaudio19-dev``
8. Install pi-clap pip module ``pip3 install pi-clap``

Now the Raspberry Pi is ready use Pi Clap

Use following code for Pi Clap to start listening. Make the necessary adjustments in the code and values to match your microphone and pinout. You can also add more methods in the derived classes.

.. literalinclude:: ../../example/rpi.app.py
  :language: python
  :linenos:

Finally run you code with ``python3 app.py``

Try 2 claps to Light up the connected LED for 1 sec and 3 claps to toggle ON/OFF state of the connected LED. Also, Use 4 claps to exit from the system.

References
----------

1. https://raspberrytips.com/add-microphone-raspberry-pi/
2. https://www.raspberrypi.org/documentation/configuration/
3. http://www.raspberrypi.org/documentation/installation/installing-images/
4. https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/instructions
5. http://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876
