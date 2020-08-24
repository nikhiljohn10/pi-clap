from munch import DefaultMunch as Objectify
from piclap.controller import Controller

class Settings():
    def __init__(self, controller=None):
        self.controller = controller or Controller()
        self.exit = False
        self.rate = 44100                   # Number of sample collected in 1sec
        self.channels = 1                   # 1 = Mono Channel
        self.chunk_size = 1024              # Number of frames in the buffer
        self.interval = 0.5                 # Interval between each clap
        self.method = Objectify.fromDict({  # Method used to identify claps
            'name': 'threshold',
            'value': 7000
        }, False)
        self.actions = [m for m in dir(self) if m.startswith(
            'on') and m.endswith('Claps')]

    def on2Claps(self):
        self.pi.flashLight(pin=13)
        print("Flashed light")

    def on3Claps(self):
        self.pi.toggleLight(pin=24)
        print("Toggled light")

    def on4Claps(self):
        self.exit = True

    def updateMethod(self, method):
        self.method = Objectify.fromDict(method, False)
