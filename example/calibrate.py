#!/usr/bin/python3

import re
from piclap import *
from time import sleep
from array import array

chunkSizeCalibrated = False
config = Settings()

def readFrom(listener):
  avg = agg = count = prv = 0
  exitCount = 200
  exit = False
  while not exit:
    data = listener.stream.read(listener.config.chunk_size)
    byte_stream = array('b', [0]) if data == None else data
    count += 1
    agg += max(array('h', byte_stream))
    avg = int(agg/count)
    if avg > prv:
      prv = avg
      print(avg)
    if count == exitCount:
      print(exitCount," samples taken.")
      exit = True
  return avg

def main():
  try:
    valley = 0
    while not valley:
      try:
        l = Listener(config)
        print("Current chunk size is",config.chunk_size)
        print("Starting calibration...\nDO NOT CLAP NOW")
        valley = readFrom(l)
      except OSError as e:
        print("Error:", e)
        if re.search(r'.+Input overflowed$', str(e)):
          config.chunk_size = int(config.chunk_size/2)
    exit = False
    l.stop()
    l = Listener(config)
    print("START CLAPPING NOW\nFinding peak value...")
    peak = count = 0
    exitCount = 1000
    while not exit:
      data = l.stream.read(config.chunk_size)
      byte_stream = array('b', [0]) if data == None else data
      maximum = max(array('h', byte_stream))
      count += 1
      if maximum > peak:
        peak = maximum
        print(peak)
      if count == exitCount:
        print(exitCount," samples taken.")
        exit = True
    print("\n\nThreshold should be set between", int((valley*2)+(peak/2)), "and", peak)
    print("Chunk size should be set to",config.chunk_size,"\n\n")
  except(KeyboardInterrupt, SystemExit):
    pass
  l.stop()

if __name__ == '__main__':
  main()