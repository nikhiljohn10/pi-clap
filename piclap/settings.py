from munch import DefaultMunch as Objectify


class Settings():
    def __init__(self):
        self.rate = 44100                   # Number of sample collected in 1sec
        self.channels = 1                   # 1 = Mono Channel
        self.chunk_size = 1024              # Number of frames in the buffer
        self.interval = 0.5                 # Interval between each clap
        self.method = Objectify.fromDict({  # Method used to identify claps
            'name': 'threshold',
            'value': 7000
        })
        self.pin = 24
