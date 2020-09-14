from munch import DefaultMunch as Objectify


class Settings:
    """This class describes all the configurations needed for the :class:`Listener` to work.

    :var boolean exit: Exit flag the determine the exit state of :class:`Listener`
    :var int rate: Bitrate at which input audio is streamed
    :var int channels: Number of audio channels used by :class:`Listener`
    :var int chunk_size: Frame count inside the audio buffer
    :var float wait: Clap wait in seconds

    :var method: The algorithm used for the detection of claps
    :vartype method: class: `Munch`
    :var actions: Collection of defined actions
    :vartype actions: list(str)
    """

    def __init__(self):
        """Constructor method"""
        self.exit = False
        """**default:** ``False``

        Exit flag
        """
        self.rate = 44100
        """**default:** ``44100``

        Number of audio samples collected in 1 second"""
        self.channels = 1
        """**default:** ``1`` (Mono Channel)

        Number of audio channel to listen"""
        self.chunk_size = 1024
        """**default:** ``1024``

        Number of frames in the input audio buffer"""
        self.wait = 0.5
        """**default:** ``0.5``

        Time duration to wait for claps to complete in :meth:`Listener.clapWait()`"""
        self.method = Objectify.fromDict({
            'name': 'threshold',
            'value': 512
        }, False)
        """**default:** :code:`{'name': 'threshold','value': 7000}`

        Detection method used for identifing claps"""
        self.actions = [m for m in dir(self) if m.startswith(
            'on') and m.endswith('Claps')]
        """When the class initialised, it collects all the actions defined inside this class as well as any classes where are derived with this class as base class

        **Condition:** *The method name defined should start with 'on' and end with 'Claps' with the clap count inbetween them.*
        """

    def on2Claps(self):
        """Action performed when 2 claps are detected."""
        print("Flashed light")

    def on3Claps(self):
        """Action performed when 3 claps are detected."""
        print("Toggled light")

    def on4Claps(self):
        """Action performed when 4 claps are detected. As default, :attr:`exit` flag is set to ``True`` if 4 claps are detected"""
        self.exit = True

    def updateMethod(self, method):
        """Update the method for detecting clap

        :param dict method: A dict type parameter which defines a clap detection method
        """
        self.method = Objectify.fromDict(method, False)
