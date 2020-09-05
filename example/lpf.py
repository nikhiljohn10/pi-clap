import os
import sys
sys.path.append(os.path.abspath('.'))
from piclap import *
import numpy as np  # 1.19.1
import matplotlib.pyplot as plt  # 3.3.1
from scipy import signal  # 1.5.2
from array import array
import multiprocessing as mp
import random
import pprint
import time
import itertools


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
        plt.ylim([np.min(y1_data) - np.std(y1_data),
                  np.max(y1_data) + np.std(y1_data)])
    plt.pause(pause_time)
    return line

# def plotter(x,y,line):
#     if line == []:
#         plt.ion()
#         fig = plt.figure(figsize=(13, 6))
#         ax = fig.add_subplot(111)
#         line, = ax.plot(x, y, '-,', alpha=0.8)
#         plt.title('Signal')
#         plt.show()
#     line.set_ydata(y)
#     plt.pause(0.5)
#     return line


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
        self.chunk_size = 1024
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


'''
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




    size = 1024
    fs = 44100
    duration = 5
    f = 100
    try:
        p = mp.Pool()
        # sample = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)
        #           ).astype(np.float32)
        # signal = list(chunks(sample, size))
'''


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]





# for y_vec in y_arr:

#line = plotter(x_vec, y_vec, line)


def plotter(q, x, y0):
    try:
        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        ln, = ax.plot(x, y0, '-,', alpha=0.8)
        fig.canvas.draw()
        plt.show(block=False)
        plt.pause(0.001)
        while True:
            y = q.get()
            old_data = ln.get_ydata()
            point = np.array(y)
            print(y)
            ln.set_ydata(np.append(old_data[1:], point))
            ax.relim()
            ax.autoscale_view(True, True, True)
            fig.canvas.draw()
            q.task_done()
            plt.pause(0.001)
    except:
        print("\rExiting")


def process(q, l):
    while True:
        for ya in getYVec(l):
            for y in ya:
                # q.put(y)
                print(y)

def getXVec(lr):
    return np.linspace(0, 1, lr.config.chunk_size + 1)[0:-1]


def getYVec(lr):
    data = lr.device.readData()
    intArr = array('h', data)
    return intArr

if __name__ == '__main__':
    c = Config()
    l = Listener(c, False)
    try:
        l.device.openStream()
        x_vec = getXVec(l)
        y_vec = getYVec(l)
        with mp.Pool() as pool:
            m = mp.Manager()
            q = m.Queue()
            result = pool.apply_async(process, (q, l,))
            result.get()
    except(KeyboardInterrupt, SystemExit):
        pass
    l.stop()
    # mp.Process(target=plotter, args=(q, x_vec, y_vec,)).start()
    # r = p.apply_async(process, (q, l,))
    # r.get()
    # p.terminate()
    # p.join()


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
