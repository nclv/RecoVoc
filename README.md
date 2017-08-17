<p align="center">

  <h1 align="center">RecoVoc</h1>

  <p align="center">
    Projet de reconnaissance vocale développé en Python avec intégration de la souris.
  </p>
</p>

## Status
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2cd632423fed43b3be7294659e4ab71e)](https://www.codacy.com/app/NicovincX2/Battleship?utm_source=github.com&utm_medium=referral&utm_content=NicovincX2/Battleship&utm_campaign=badger)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)
![Supported Versions](https://img.shields.io/badge/python-3.3%2C%203.4%2C%203.5%2C%203.6-blue.svg)


## Installation
Les versions de Python inférieures à Python3 ne sont pas supportées.  
Pour installer les modules utilisés dans le programme, voir tout d'abord les dépendances du module ```SpeechRecognition``` [ici](https://github.com/Uberi/speech_recognition#requirements), ainsi que celles du module ```pyttsx3``` [ici](http://pyttsx.readthedocs.io/en/latest/install.html) sur Windows.  
Exécuter ensuite la commande qui suit pour installer les modules Python.
```python
pip3 install -r requirements.txt
```  
En cas d'erreur lors de l'installation du module ```pyuserinput```, consulter la [liste](https://github.com/SavinaRoja/PyUserInput#dependencies) de dépendances de ce package.  
Si les modules Python nécessaires ne sont pas installés, le lancement de ```speech.py``` les installera automatiquement via ```pip3```.  

En cas d'erreurs lors de l'utilisation de type ```pcm_dmix``` sous Linux, suivre la procédure suivante.   
*Create a file called /etc/modprobe.d/default.conf with this content:*
```
options snd_hda_intel index=1
```
*Then reboot.*

## Description
Un micro est nécessaire à la reconnaissance vocale.
