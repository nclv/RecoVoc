<p align="center">

  <h1 align="center">RecoVoc</h1>

  <p align="center">
    Projet de reconnaissance vocale développé en Python avec intégration de la souris.
  </p>
</p>

## Status
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2cd632423fed43b3be7294659e4ab71e)](https://www.codacy.com/app/NicovincX2/Battleship?utm_source=github.com&utm_medium=referral&utm_content=NicovincX2/Battleship&utm_campaign=badger)

## Installation
Pour installer les modules utilisés dans le programme, voir tout d'abord les dépendances du module ```speech_recognition``` [ici](https://github.com/Uberi/speech_recognition#requirements) et les installer.
Exécuter ensuite la commande qui suit pour installer les modules Python.
```python
pip install -r requirements.txt
```
En cas d'erreur lors de l'installation du module ```pyuserinput```, consulter la [liste](https://github.com/SavinaRoja/PyUserInput#dependencies) de dépendances de ce package.  
Si les modules Python nécessaires ne sont pas installés, le lancement de ```speech.py``` les installera auomatiquement via ```pip```.  
Si ```pip``` n'est pas reconnu que l'erreur renvoyée est de type: ```'python pip' is not recognized as an internal or external command, operable program or batch file.```.  
Voir [pip is not recognized](https://github.com/Langoor2/PokemonGo-Map-FAQ/wiki/%27python---pip%27-is-not-recognized-as-an-internal-or-external-command,-operable-program-or-batch-file) pour ajouter le répertoire ```Scripts``` de votre répertoire Python au ```path```.  

En cas d'erreurs lors de l'utilisation de type ```pcm_dmix```, suivre la procédure suivante.  
Create a file called /etc/modprobe.d/default.conf with this content:
```
options snd_hda_intel index=1
```
Then reboot.

## Description
Un micro est nécessaire à la reconnaissance vocale.
