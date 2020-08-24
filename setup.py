"""

    ###################
    ##               ##
    ##    Pi-Clap    ##
    ##               ##
    ###################

Repo: https://github.com/nikhiljohn10/pi-clap
Author: Nikhil John
License: MIT
"""
from piclap import __project__ as PROJECT, __author__ as AUTHOR, __release__ as VERSION

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=PROJECT,
    version=VERSION,
    author=AUTHOR,
    author_email="ceo@jwala.diamonds",
    description="A python package for clap detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikhiljohn10/pi-clap",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    platforms="any",
    py_modules=['piclap'],
    python_requires='>=3.6',
    install_requires=[
        "pyaudio>=0.2.11",
        "munch>=2.5.0",
    ],
)
