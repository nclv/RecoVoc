#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""messages.py: Messages de l'application RecoVoc."""

from textblob import TextBlob, exceptions

mess_fr = {
    "start": TextBlob("Dites quelque chose !"),
    "google_understand": TextBlob("Google Speech Recognition n'a pas pu comprendre l'audio."),
    "google_request": TextBlob("Ne peut pas demander les résultats du service de reconnaissance vocale Google; {}"),
    "wit_understand": TextBlob("Wit.ai n'a pas pu comprendre l'audio."),
    "wit_request": TextBlob("Ne peut pas demander les résultats du service de reconnaissance vocale Wit.ai; {}"),
    "diff_understand": TextBlob("Les différents services de reconnaissance n'ont pas compris la même chose."),
    "check_one_audio": TextBlob("Avez-vous voulu dire {} ?"),
    "check_none_audio": TextBlob("Avez-vous voulu dire une des sentences suivantes ?"),
    "calibrating": TextBlob("Attendez s'il vous plait. Calibration du microphone...")
}

try:
    mess_en = {key: text.translate(from_lang=text.detect_language(), to='en') for key, text in mess_fr.items()}
except exceptions.NotTranslated:
    pass
