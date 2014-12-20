#!/usr/bin/python
import pyaudio
import sys
import thread
from time import sleep
from array import array
import RPi.GPIO as GPIO

clap = 0
wait = 2
flag = 0
pin = 24
exitFlag = False	

def toggleLight(c):
	GPIO.output(c,True)
	sleep(1)
	GPIO.output(c,False)
	print("Light toggled")

def waitForClaps(threadName):
	global clap
	global flag
	global wait
	global exitFlag
	global pin
	print "Waiting for more claps"
	sleep(wait)
	if clap == 2:
		print "Two claps"
		toggleLight(pin)
	# elif clap == 3:
	# 	print "Three claps"
	elif clap == 4:
		exitFlag = True
	print "Claping Ended"
	clap = 0
	flag = 0

def main():
	global clap
	global flag
	global pin

	chunk = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	threshold = 3000
	max_value = 0
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
					channels=CHANNELS, 
					rate=RATE, 
					input=True,
					output=True,
					frames_per_buffer=chunk)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	try:
		print "Clap detection initialized"
		while True:
			data = stream.read(chunk)
			as_ints = array('h', data)
			max_value = max(as_ints)
			if max_value > threshold:
				clap += 1
				print "Clapped"
			if clap == 1 and flag == 0:
				thread.start_new_thread( waitForClaps, ("waitThread",) )
				flag = 1
			if exitFlag:
				sys.exit(0)
	except (KeyboardInterrupt, SystemExit):
		print "\rExiting"
		stream.stop_stream()
		stream.close()
		p.terminate()
		GPIO.cleanup()

if __name__ == '__main__':
	main()
