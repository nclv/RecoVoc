<h1 align="center">RecoVoc</h1>
<h4 align="center">Projet de reconnaissance vocale développé en Python avec intégration de la souris.</h4>

## Status
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2cd632423fed43b3be7294659e4ab71e)](https://www.codacy.com/app/NicovincX2/Battleship?utm_source=github.com&utm_medium=referral&utm_content=NicovincX2/Battleship&utm_campaign=badger)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)
![Supported Versions](https://img.shields.io/badge/python-3.3%2C%203.4%2C%203.5%2C%203.6-blue.svg)

## Installation 
Pour installer les modules utilisés dans le programme, voir tout d'abord les dépendances du module ```SpeechRecognition``` [ici](https://github.com/Uberi/speech_recognition#requirements), ainsi que celles du module ```pyttsx3``` [ici](http://pyttsx.readthedocs.io/en/latest/install.html) sur Windows.  
Sur la ligne de commande:
```bash
pip3 install -r requirements.txt
```  
En cas d'erreur lors de l'installation du module ```pyuserinput```, consulter la [liste](https://github.com/SavinaRoja/PyUserInput#dependencies) de dépendances de ce package.  
 

En cas d'erreurs lors de l'utilisation de type ```pcm_dmix``` sous Linux, suivre la procédure suivante.

*Create a file called /etc/modprobe.d/default.conf with this content:*
```
options snd_hda_intel index=1
```
*Then reboot.*

## Description

## Download

## Credits

Ce programme utilise les modules Python suivants:

 - [SpeechRecognition](https://github.com/Uberi/speech_recognition)
 - [PyUserInput](https://github.com/SavinaRoja/PyUserInput)
 - [pytssx3](https://github.com/nateshmbhat/pyttsx3)
