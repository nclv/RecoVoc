#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import apt

from setuptools import setup, find_packages
from setuptools.command.install import install

import recovoc


here = os.path.abspath(os.path.dirname(__file__))

class CustomInstallCommand(install):
    """Customized setuptools install command."""
    def run(self):
        """Installation des dépendances (Linux).
        """

        # First of all, open the cache
        cache = apt.Cache()
        # Now, lets update the package list
        cache.update()
        # We need to re-open the cache because it needs to read the package list
        cache.open(None)
        my_selected_packages = [cache["python-dev"], cache["portaudio19-dev"], cache["ffmpeg"]]
        with cache.actiongroup():
            for package in my_selected_packages:
                package.mark_install()

        install.run(self)

long_description = open('README.md').read()

setup(
    name='RecoVoc',
    version=recovoc.__version__,
    description="Reconnaissance vocale",
    long_description=long_description,
    license=recovoc.__licence__,
    author=recovoc.__author__,
    author_email='nicolas.vincent100@gmail.com',
    url='https://github.com/NicovincX2/RecoVoc',
    download_url='https://github.com/NicovincX2/RecoVoc/archive/%s.tar.gz' % recovoc.__version__,
    keywords='tts stt python3 speech-recognition',
    install_requires=['textblob', 'pygame', 'pyuserinput','pyaudio', 'SpeechRecognition', 'pyttsx3'],
    python_requires='>=3.3',
    packages=find_packages('recovoc', exclude=['Images', 'Snaps', 'Videos']),
    package_dir={'Recovoc': 'recovoc'},
    cmdclass={'install': CustomInstallCommand},
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: French",
        "Operating System :: POSIX :: Linux",
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
