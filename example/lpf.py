import numpy as np  # 1.19.1
import matplotlib.pyplot as plt  # 3.3.1
from scipy import signal  # 1.5.2
from array import array
import os
import sys
sys.path.append(os.path.abspath('.'))

from piclap import *

# use ggplot style for more sophisticated visuals
plt.style.use('fast')


def live_plotter(x_vec, y1_data, line, identifier='', pause_time=0.05):
    if line == []:
        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        line, = ax.plot(x_vec, y1_data, '-,', alpha=0.8)
        plt.title('{}'.format(identifier))
        plt.show()
    line.set_ydata(y1_data)
    if np.min(y1_data) <= line.axes.get_ylim()[0] or np.max(y1_data) >= line.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data) - np.std(y1_data), np.max(y1_data) + np.std(y1_data)])
    plt.pause(pause_time)
    return line

def pylive():
    size = 100
    x_vec = np.linspace(0, 1, size + 1)[0:-1]
    y_vec = np.random.randn(len(x_vec))
    line = []
    while True:
        rand_val = np.random.randn(1)
        y_vec[-1] = rand_val
        line = live_plotter(x_vec, y_vec, line)
        y_vec = np.append(y_vec[1:], 0.0)

class Config(Settings):
    def __init__(self):
        Settings.__init__(self)
        self.chunk_size = 2048
        self.method.value = 10000


def getXVec(lr):
    return np.linspace(0, 1, lr.config.chunk_size + 1)[0:-1]

def getYVec(lr):
    # try:
    #     data = lr.device.readData()
    # except (OSError, IOError):
    #     data = array('b', [0])
    data = lr.device.readData()
    intArr = array('h', data)
    return intArr

try:
    c = Config()
    l = Listener(c, False)
    try:
        line = []
        l.device.openStream()
        x_vec = getXVec(l)
        y_vec = getYVec(l)
        print(y_vec)
        while True:
            # vmax = max(getYVec(l))
            # y_vec[-1] = vmax
            # print(vmax)
            # line = live_plotter(x_vec, y_vec, line)
            # y_vec = np.append(y_vec[1:], 0.0)
            line = live_plotter(x_vec, y_vec, line)
            y_vec = getYVec(l)
            print(y_vec)

    except(KeyboardInterrupt, SystemExit):
        pass
    l.stop()
except(KeyboardInterrupt, SystemExit):
    print("\rExiting Plotter")














'''
fs = 44100.0  # Sampling frequency
# Generate the time vector properly
t = np.arange(4000) / fs
signala = np.sin(2*np.pi*100*t) # with frequency of 100
plt.plot(t, signala, label='a')

signalb = np.sin(2*np.pi*20*t) # frequency 20
plt.plot(t, signalb, label='b')

signalc = signala + signalb
plt.plot(t, signalc, label='c')

fc = 30  # Cut-off frequency of the filter
w = int(fc / (fs / 2)) # Normalize the frequency
b, a = signal.butter(4, w, 'low', fs=fs)
output = signal.filtfilt(b, a, signalc)
plt.plot(t, output, label='filtered')
plt.legend()
plt.show()
'''
