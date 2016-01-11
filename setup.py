import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "tox-example",
    version = "0.0.1",
    author = "Ferenc Beres",
    packages=['scripts','tests']
)
