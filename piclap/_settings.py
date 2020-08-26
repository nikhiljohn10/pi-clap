from munch import DefaultMunch as Objectify


class Settings:
    """This class describes all the configurations needed for the :class:`piclap.Listener` to work.

    :param controller: A :class:`piclap.Controller` object, defaults to None
    :type controller: class: `piclap.Controller`
    :var controller: Holds the controller object passed as argument
    :vartype controller: class: `piclap.Controller`
    :var boolean exit: Holds the controller object passed as argument
    :var int rate: Holds the controller object passed as argument
    :var int channels: Holds the controller object passed as argument
    :var int chunk_size: Holds the controller object passed as argument
    :var float interval: Holds the controller object passed as argument

    :var method: Holds the controller object passed as argument
    :vartype method: class: `piclap.Controller`
    :var actions: Holds the controller object passed as argument
    :vartype actions: class: `piclap.Controller`
    """

    def __init__(self, controller=None):
        """Constructor method"""
        self.controller = controller  # Updated docs
        """If the :attr:`controller` parameter is ``None``, an object of :class:`piclap.Controller` is assigned"""
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
        self.interval = 0.5
        """**default:** ``0.5``

        Time duration to wait inside :meth:`piclap.Listener.clapWait()`"""
        self.method = Objectify.fromDict({
            'name': 'threshold',
            'value': 7000
        }, False)
        """**default:** :code:`{'name': 'threshold','value': 7000}`

        Detection method used for identifing claps"""
        self.actions = [m for m in dir(self) if m.startswith(
            'on') and m.endswith('Claps')]
        """When the class initialised, it collects all the actions defined inside this class as well as any classes where are derived with this class as base class

        **Condition:** __The method name defined should start with 'on' and end with 'Claps' with the clap count inbetween them.__
        """

    def on2Claps(self):
        """Action performed when 2 claps are detected. As default, it call the method :meth:`piclap.Controller.flashLight` on pin 13"""
        self.pi.flashLight(pin=13)
        print("Flashed light")

    def on3Claps(self):
        """Action performed when 3 claps are detected. As default, it call the method :meth:`piclap.Controller.toggleLight` on pin 24"""
        self.pi.toggleLight(pin=24)
        print("Toggled light")

    def on4Claps(self):
        """Action performed when 4 claps are detected. As default, :attr:`exit` flag is set to ``True`` if 4 claps are detected"""
        self.exit = True

    def updateMethod(self, method):
        """Update the method for detecting clap

        :param dict method: A dict type parameter which defines a clap detection method
        """
        self.method = Objectify.fromDict(method, False)
