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


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pi-clap",
    version="1.1",
    author="Nikhil John",
    author_email="ceo@jwala.diamonds",
    description="A clap detection and signalling package created for Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikhiljohn10/pi-clap",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    platforms="any",
    py_modules=['piclap'],
    python_requires='>=3.6',
    install_requires=[
        "pyaudio>=0.2.11",
        "munch>=2.5.0",
    ],
)
