#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import platform
import io

from setuptools import setup, find_packages

import speech

# Vérification de la version de l'installation
try:
    assert sys.version_info >= (3,0)
except AssertionError:
    raise SystemExit("Ce programme ne supporte pas Python {}. Installer une version supérieure pour le faire tourner.".format(platform.python_version()))


here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    """Lit plusieurs fichiers et les assemble.
    """

    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

setup(
    name='RecoVoc',
    version=speech.__version__,
    description="Reconnaissance vocale.",
    long_description=long_description,
    license=speech.__licence__,
    author=speech.__author__,
    author_email='nicolas.vincent100@gmail.com',
    url='https://github.com/NicovincX2/RecoVoc',
    install_requires=['textblob', 'pyuserinput','pyaudio', 'SpeechRecognition', 'pyttsx3'],
    packages=find_packages(exclude=['docs']),
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: French",
        "Operating System :: OS Independent"
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Home Automation",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
    ],
)
