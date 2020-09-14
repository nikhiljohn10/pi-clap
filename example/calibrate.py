#!/usr/bin/python3

import re
from piclap import *
from time import sleep
from array import array

config = Settings()

def getMax(l):
  data = l.stream.read(l.config.chunk_size)
  byte_stream = array('b', [0]) if data == None else data
  maximum = max(array('h', byte_stream))
  return maximum

def testExit(c, e):
  if c > e:
    print(e," samples taken.")
    return True
  return False

def main():

  # Calibrating chunk size and detecting valley point

  try:
    valley = peak = 0
    while not valley:
      print("Starting calibration...\nDO NOT CLAP OR MAKE ANY NOISE NOW")
      try:
        listener = Listener(config)
        avg = agg = count = prv = 0
        exit = False
        print("Tesing with chunk size:",listener.config.chunk_size)
        while not exit:
          count += 1
          agg += getMax(listener)
          avg = int(agg/count)
          if avg > prv:
            prv = avg
            print(avg)
          exit = testExit(count, 200)
        valley = avg
      except OSError as e:
        print("Error:", e)
        if re.search(r'.+Input overflowed$', str(e)):
          config.chunk_size = int(config.chunk_size/2)
    listener.stop()

    # Calibrating clap threshold

    print("START CLAPPING NOW\nFinding peak value...")
    listener = Listener(config)
    count = 0
    exit = False
    while not exit:
      maximum = getMax(listener)
      count += 1
      if maximum > peak:
        peak = maximum
        print(peak)
      exit = testExit(count, 1000)

      # Result

    print("\n\nThreshold should be set between", int((valley*2)+(peak/2)), "and", peak)
    print("Chunk size should be set to",config.chunk_size,"\n\n")
  except(KeyboardInterrupt, SystemExit):
    pass
  listener.stop()

if __name__ == '__main__':
  main()
