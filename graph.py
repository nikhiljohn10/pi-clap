import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import numpy as np
import wave
import zipfile


NFFT = 1024  # the length of the windowing segments
COUNT = 23
output = []


def plot(id, signal, time, Fs):
    max_val = np.amax(np.absolute(signal))

    fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(8, 6))
    plt.subplots_adjust(hspace=0.25)

    ax1.plot(time, signal)
    ax1.set_xlabel('Time [second]')
    ax1.set_yticks([-max_val, -max_val / 2, 0, max_val / 2, max_val])
    ax1.set_yticklabels(['-1.0', '-0.5', '0', '0.5', '1.0'])
    ax1.set_ylabel('Amplitude')

    freqFormatter = EngFormatter(unit='Hz')
    ax2.yaxis.set_major_formatter(freqFormatter)
    Pxx, freqs, bins, im = ax2.specgram(signal, NFFT=NFFT, Fs=Fs)
    ax2.set_xlabel('Time [second]')
    ax2.set_ylabel('Frequency [Hz]')

    # plt.show()
    fig.savefig('output/{:02d}.png'.format(id))
    plt.close(fig)

    return (Pxx, freqs, bins, im)


def process(id, file):
    signal = file.readframes(-1)
    signal = np.frombuffer(signal, dtype=np.int16)

    Fs = file.getframerate()
    t = np.linspace(0, float(len(signal)) / Fs, num=len(signal))
    output.append(plot(id, signal, t, Fs))


def main():
    with zipfile.ZipFile('samples.zip', 'r') as zipper:
        zipper.extractall('.')
    try:
        for id in range(0, COUNT + 1):
            filename = 'samples/{:02d}.wav'.format(id)

            with wave.open(filename, "r") as file:
                if file.getnchannels() == 2:
                    print(filename, "is not a mono audio file")
                    continue
                print(filename, "is opened and being processed")
                process(id, file)
    except(KeyboardInterrupt):
        print("\rExiting")


if __name__ == '__main__':
    main()
