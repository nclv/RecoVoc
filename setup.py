#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import platform
import io

from setuptools import setup, find_packages
from setuptools.command.install import install

from recovoc import speech


here = os.path.abspath(os.path.dirname(__file__))

class CustomInstallCommand(install):
    """Customized setuptools install command."""
    def run(self):
        os.system("apt install python-dev portaudio19-dev")
        install.run(self)

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
    keywords='tts stt python3 speech-recognition',
    install_requires=['textblob', 'pygame', 'pyuserinput','pyaudio', 'SpeechRecognition', 'pyttsx3'],
    python_requires='>=3.3',
    packages=find_packages('recovoc', exclude=['Images', 'Snaps', 'Videos']),
    package_dir={'': 'recovoc'},
    cmdclass={'install': CustomInstallCommand},
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: French",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Home Automation",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
    ],
    test_suite='tests',
)
