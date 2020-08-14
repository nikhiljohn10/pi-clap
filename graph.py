import wave
import shutil
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


class Plotter():

    def __init__(self):
        fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(8, 6))
        self.figure = fig
        self.waveplot = ax1
        self.specplot = ax2

    def __del__(self):
        plt.close(self.figure)

    def processFile(self, file):
        data = file.readframes(-1)
        self.rate = file.getframerate()
        self.signal = np.frombuffer(data, dtype=np.int16)
        self.max_val = np.amax(np.absolute(self.signal))
        self.time = np.linspace(0,
                                float(len(self.signal)) / self.rate,
                                num=len(self.signal))

    def setupPlot(self):
        plt.subplots_adjust(hspace=0.25)
        self.waveplot.set_xlabel('Time [second]')
        self.waveplot.set_ylabel('Amplitude')
        self.waveplot.set_yticks([-self.max_val,
                                  -self.max_val / 2,
                                  0,
                                  self.max_val / 2,
                                  self.max_val])
        self.waveplot.set_yticklabels(['-1.0', '-0.5', '0', '0.5', '1.0'])
        self.specplot.yaxis.set_major_formatter(EngFormatter(unit='Hz'))
        self.specplot.set_xlabel('Time [second]')
        self.specplot.set_ylabel('Frequency [Hz]')

    def writeData(self, path, data):
        Pxx, freqs, bins, im = data
        shutil.os.mkdir(path)
        np.savetxt(path + '/periodogram.dat', Pxx)
        np.savetxt(path + '/freqs.dat', freqs)
        np.savetxt(path + '/time_bins.dat', bins)
        self.figure.savefig(path + '/plot.jpg', format='jpg', dpi=150)

    def print(self, id, file):
        self.processFile(file)
        self.setupPlot()
        self.waveplot.plot(self.time, self.signal)
        spectrum = self.specplot.specgram(self.signal,
                                          NFFT=1024,
                                          Fs=self.rate)
        # plt.show()
        self.writeData('./output/{:02d}'.format(id), spectrum)


def main():
    fs_error = False
    try:
        shutil.rmtree('./output', ignore_errors=True)
        shutil.os.mkdir('./output')
        shutil.unpack_archive('samples.zip', '.')
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))
        fs_error = True
    if not fs_error:
        try:
            for id in range(0, 24):
                filename = 'samples/{:02d}.wav'.format(id)
                with wave.open(filename, "r") as file:
                    if file.getnchannels() == 2:
                        print(filename, "is not a mono audio file")
                        continue
                    print(filename, "is opened and being processed")
                    plot = Plotter()
                    plot.print(id, file)
        except(KeyboardInterrupt):
            print("\rExiting")
        shutil.rmtree('./samples', ignore_errors=True)


if __name__ == '__main__':
    main()
