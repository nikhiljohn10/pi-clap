"""A python package for clap detection

.. module:: pi-clap
   :platform: All
   :synopsis: A clap detection python module

.. moduleauthor:: Nikhil John <ceo@jwala.diamonds>

"""
from ._settings import Settings
from ._listener import Listener
from ._controller import Controller

__project__ = 'pi-clap'
__version__ = '1.2.1b'
__author__ = 'Nikhil John'
__all__ = ['Settings', 'Listener', 'Controller']
