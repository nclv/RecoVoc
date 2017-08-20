#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""speech.py: Programme de reconnaissance vocale."""

__version__='1.0.0'
__author__ = "VINCENT Nicolas"
__licence__ = "GPLv3"

import os
import sys
import time
import timeit #timer
import logging
import itertools

import utils
import camera


try:
    import messages #Textblob
    from pymouse import PyMouse
    import speech_recognition as sr
    import pyttsx3
except ImportError as e:
    print(e)
    import subprocess
    subprocess.run(["pip3", "install", "-r", "requirements.txt"])
    raise SystemExit()


class Recognition(object):
    """Classe de reconnaissance vocale.

    Attributes:

    """

    def __init__(self):
        """Initialisation de la Classe.

        Args:

        .. seealso:: speech_recognition(module)
        """
        # Initialisation de pyttsx3, conservation des changements (rate, language) pour la fonction say()
        self.voiceEngine = pyttsx3.init('espeak')
        self.voiceEngine.setProperty('rate', self.voiceEngine.getProperty('rate')-40)

        self.language, self.wit_key = self.choose_lang()

        self.reco_services = self.choose_services()
        # TODO: Put in a dict in messages.py
        self.commands = ['next','stop']
        self.sample_history = []
        self.time_start = timeit.default_timer()
        self.exit = False

        self.logging_config()

        recogniz = sr.Recognizer()
        micro = sr.Microphone()
        with micro as source:
            self.say(self.messages["calibrating"])
            recogniz.adjust_for_ambient_noise(source, duration=1)  # we only need to calibrate once, before we start listening
            # Evite de nombreux faux-négatifs (détecte à 5 fois du volume ambiant)
            recogniz.dynamic_energy_ratio = 5 # Premier mot prononcé fort pour atteindre le niveau de déclenchement
            time.sleep(2)
            self.say(self.messages["start"])

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
            sr.RequestError: Ne peut pas utiliser les services de reconnaissance de l'API.
        """

        self.services_recognition(recognizer, audio)
        # On sort si la liste est vide
        if not self.sample_list: return
        self.check_audio()

        self.mouse_actions()

    def services_recognition(self, recognizer, audio):
        """Reconnaissance vocale via différentes API.

        Args:
            recognizer: Voir speech_recognition(module).
            audio: Voir speech_recognition(module).
        """

        # Initialisation de la liste des transcriptions
        self.sample_list = [u'', u'']

        if self.reco_services is '1':
            self.reco_google(recognizer, audio)
        elif self.reco_services is '2':
            self.reco_wit(recognizer, audio)
        else:
            self.reco_google(recognizer, audio)
            self.reco_wit(recognizer, audio)

        # Enlève les strings vides
        self.sample_list = list(filter(None, self.sample_list))

    def reco_google(self, recognizer, audio):
        """Reconnaissance vocale avec les services de Google.
        """

        # Recognize audio data using Google Speech Recognition
        try:
            self.sample_list[0] = recognizer.recognize_google(audio, language=self.language)
            self.logger.info("Google Speech Recognition : " + self.sample_list[0])
        except sr.UnknownValueError:
            print(self.messages["google_understand"])
            pass
        except sr.RequestError as e:
            print(self.messages["google_request"].format(e))

    def reco_wit(self, recognizer, audio):
        """Reconnaissance vocale avec les services de Wit.ai.
        """

        # Recognize with WIT.ai
        try:
            self.sample_list[1] = recognizer.recognize_wit(audio, key=self.wit_key)
            self.logger.info("Wit.ai : " + self.sample_list[1])
        except sr.UnknownValueError:
            print(self.messages["wit_understand"])
        except sr.RequestError as e:
            print(self.messages["wit_request"].format(e))
            pass

    def check_audio(self):
        """Vérifie que la reconnaissance entre les différentes API retourne la même chose.
        """

        sample_lower = [sample.lower() for sample in self.sample_list]
        # Test différence de compréhension
        for sample_1, sample_2 in itertools.combinations(sample_lower, 2):
            if sample_1 != sample_2:
                self.say(self.messages["diff_understand"])

        # Test si un ou plusieurs samples sont dans les commandes
        numb_sample = 0
        place = []
        for index, sample in enumerate(self.sample_list):
            if sample in self.commands:
                numb_sample += 1
                place.append(index)

        if numb_sample == 1: # une commande dans sample_list
            command = self.sample_list[place[0]]
            self.say(self.messages["check_one_audio"].format(command))
        elif utils.comp_ele_list(sample_lower): # même éléments dans la liste
            self.say(self.messages["check_one_audio"].format(self.sample_list[0]))
        elif numb_sample == 0: # aucune commande
            self.say(self.messages["check_none_audio"])
            print('\n'.join('{}: {}'.format(*k) for k in enumerate(self.sample_list)))
        else: # numb_sample >= 2
            self.say(self.messages["check_none_audio"])
            print('\n'.join('{}: {}'.format(*k) for k in enumerate([self.sample_list[i] for i in place])))

    def say(self, mess):
        """Laisse parler la machine...

        Args:
            mess (str): Message à prononcer
        """

        self.voiceEngine.say(mess)
        self.voiceEngine.runAndWait()

    def mouse_actions(self):
        """Prise en charge des commandes d'interaction avec la souris.

        .. seealso:: pymouse(module)
        """

        mouse = PyMouse()

        if self.sample_list[0] == 'next':
            mouse.move(1269,419)
            mouse.click(1269,419)
        if self.sample_list[0] == 'stop':
            self.exit = True
            self.time_elapsed = utils.end_timer(self.time_start)

        if self.sample_list[0] in self.commands: self.sample_history.append(self.sample_list[0])

    @utils.while_true
    def choose_services(self):
        """Choix du service de reconnaissance vocale.
        """

        service = input(self.messages["choose_service"] + ' ')
        if service not in ['1', '2', '3']:
            raise ValueError(self.messages["verif_service"])

        return service

    @utils.while_true
    def choose_lang(self):
        """Choix du langage à utiliser, français ou anglais.
        """

        choice = input("Which language would you like to use, [French, fr] or [English, en] ?\n>> ")
        if choice.lower() in ["french", "fr"]:
            LANGAGE="fr-FR"
            self.voiceEngine.setProperty('voice', 'french')
            WIT_key = "53PPLXR2O7K5OIU5EF3ZKD4SBZIAAYJP"
            self.messages = messages.mess_fr
        elif choice.lower() in ["english", "en"]:
            LANGAGE="en-GB"
            self.voiceEngine.setProperty('voice', 'english-us')
            WIT_key = "3AIMEB635MFDOXYCXGG2IVOQ5T4GNR2W"
            print("Translating ...")
            self.messages = messages.trans_fr_en()
        else:
            raise ValueError("Entrer une langue supportée.")

        return LANGAGE, WIT_key

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

        return "\nSample List: {}\nTemps écoulé: {}\nLangue: {}".format(self.sample_history, self.time_elapsed, self.language)


# Write audio on a file
#with open("microphone-results.wav", "wb") as f:
#    f.write(audio.get_wav_data())


if __name__ == '__main__':
    sys.exit(Recognition())
