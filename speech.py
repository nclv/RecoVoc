#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""speech.py: Programme de reconnaissance vocale."""

__version__='0.1.0'

import os
import sys
import platform
import time
import timeit #Timer
import logging
import functools


# Vérification de la version de l'installation
try:
    assert sys.version_info >= (2,6)
except AssertionError:
    raise SystemExit("Ce programme ne supporte pas Python {}. Installer une version supérieure pour le faire tourner.".format(platform.python_version()))

try:
    from pymouse import PyMouse
    import speech_recognition as sr
except ImportError:
    import subprocess
    if sys.version_info >= (3,5):
        subprocess.run(["pip", "install", "-r", "requirements.txt"])
    else:
        subprocess.call("pip install -r requirements.txt", shell=True)
    raise SystemExit()


if os.path.exists("speech_coord.txt"):
    with open("speech_coord.txt", 'r') as f:
        data = f.read()
    config_list = [line.split() for line in data.splitlines()]

#print(config_list)

def end_timer(time_start):
    """Afficher le temps écoulé en format hh:mm:ss.

    Args:
        time_start (int): Début de timer.

    Returns:
        Temps écoulé.
    """

    passed = timeit.default_timer() - time_start

    m, s = divmod(passed, 60)
    h, m = divmod(m, 60)

    return "%d:%02d:%02d" % (h, m, s)

class Recognition(object):
    """Classe de reconnaissance vocale.

    Attributes:

    """

    def __init__(self):
        """Initialisation de la Classe.

        Args:

        .. seealso:: speech_recognition(module)
        """

        self.commands = ['next','stop']
        self.sample_list = []
        self.sample = ''
        self.time_start = timeit.default_timer()
        self.exit = False

        self.logging_config()

        recogniz = sr.Recognizer()
        micro = sr.Microphone()
        with micro as source:
            recogniz.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
            print("Say something!")

        # start listening in the background (note that we don't have to do this inside a `with` statement)
        stop_listening = recogniz.listen_in_background(micro, self.callback)
        # `stop_listening` is now a function that, when called, stops background listening

        while self.exit == False: time.sleep(0.1)

    def callback(self, recognizer, audio):
        """Routine d'écoute.

        Args:
            recognizer: Voir speech_recognition(module).
            audio: Voir speech_recognition(module).

        Raises:
            sr.UnknownValueError: Incompréhension de l'audio.
            sr.RequestError: Ne peut pas utiliser les services de reconnaissance de Google.
        """

        # Recognize audio data using Google Speech Recognition
        try:
            self.sample = recognizer.recognize_google(audio)
            self.logger.info("Google Speech Recognition thinks you said " + self.sample)
        except sr.UnknownValueError:
            #print("Google Speech Recognition could not understand audio")
            pass
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        # Code à exécuter en cas d'enregistrement audio
        self.mouse_actions()

    def mouse_actions(self):
        """Prise en charge des commandes d'interaction avec la souris.

        .. seealso:: pymouse(module)
        """

        mouse = PyMouse()

        if self.sample == 'next':
            mouse.move(1269,419)
            mouse.click(1269,419)
        if self.sample == 'stop':
            self.exit = True
            self.time_elapsed = end_timer(self.time_start)

        if self.sample in self.commands: self.sample_list.append(self.sample)
        self.sample = ''

    def logging_config(self):
        """Log les commandes valides dans un fichier.
        """

        logFormatter = logging.Formatter(fmt='%(asctime)s %(message)s', datefmt='%H:%M:%S')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        fileHandler = logging.FileHandler('recovoc.log', mode='w+')
        fileHandler.setFormatter(logFormatter)
        self.logger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        self.logger.addHandler(consoleHandler)

        self.logger.info("----START LOGGING----")

    def __str__(self):
        """Affichage de tous les attributs de la classe.

        Returns:

        """

        return "Sample List: {}\nTemps écoulé: {}\n".format(self.sample_list, self.time_elapsed)


# Write audio on a file
#with open("microphone-results.wav", "wb") as f:
#    f.write(audio.get_wav_data())


if __name__ == '__main__':
    sys.exit(Recognition())
