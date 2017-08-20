<h1 align="center">RecoVoc</h1>
<h4 align="center">Projet de reconnaissance vocale développé en Python avec intégration de la souris.</h4>
<img align="center" src="recovoc.png">

## Status
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/96eaf2654ab046aa8b58da549de20472)](https://www.codacy.com/app/NicovincX2/RecoVoc?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=NicovincX2/RecoVoc&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/96eaf2654ab046aa8b58da549de20472)](https://www.codacy.com/app/NicovincX2/RecoVoc?utm_source=github.com&utm_medium=referral&utm_content=NicovincX2/RecoVoc&utm_campaign=Badge_Coverage)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)
![Supported Versions](https://img.shields.io/badge/python-3.3%2C%203.4%2C%203.5%2C%203.6-blue.svg)

## Pour commencer
S'assurer d'avoir les différents modules installés ainsi que leur dépendances.
```bash
git clone https://github.com/NicovincX2/RecoVoc #Cloner le répertoire
cd RecoVoc/
python3 setup.py install #Pour l'installation des dépendances
python3 speech.py #Pour lancer le programme
```

# Prérequis
En cas d'erreur lors de l'installation consulter la liste de dépendances des modules utilisés.  
- [PyUserInput](https://github.com/SavinaRoja/PyUserInput#dependencies)
- [SpeechRecognition](https://github.com/Uberi/speech_recognition#requirements)
- [pyttsx3](http://pyttsx.readthedocs.io/en/latest/install.html)

Pour utiliser les options vidéos, le module ```ffmpeg``` est nécessaire. Sur Windows, le télécharger sur leur site officiel et suivre les instructions d'installation.  
Sur Linux:
```bash
apt install ffmpeg
```

# Installation  
Sur la ligne de commande:
```bash
python3 setup.py install
```  
En cas d'erreurs lors de l'utilisation de type ```pcm_dmix``` sous Linux, suivre la procédure suivante.

*Create a file called /etc/modprobe.d/default.conf with this content:*
```
options snd_hda_intel index=1
```
*Then reboot.*

## Description
 - Sur un portable, garder le volume de votre appareil en dessous d'une certaine limite à déterminer pour éviter les fausses détection vocales liées au retour d'audio.
 - Les frappes du clavier peuvent être détectées par Wit.ai dans la version anglaise du programme.

 On constate quelquefois une interprétation erronée de bruit par Wit.ai alors que Google ne comprends pas l'audio. Il peut alors être souhaitable de modifier le paramètre ```recogniz.dynamic_energy_ratio = 5``` vers une valeur plus élevée.

### Fichiers
 - ```speech.py```: Code de base à exécuter.
 - ```messages.py```: Messages de l'application.
 - ```utils.py```: Fonctions utiles.
 - ```camera.py```: Intégration de la caméra.
 - ```recovoc.log```: Log des actions via le module logging.

### Dossiers
 - ```Images```: Images prises par la camera, ```cap-default``` sera écrasée si ```new=False```.
 - ```Snaps```: Images nécessaires à la création d'une vidéo, elles sont écrasées avant une nouvelle vidéo.
 - ```Videos```: Même fonctionnement que pour le dossier ```Images```.

## Download

## Credits
Ce programme utilise les modules Python suivants:

 - [SpeechRecognition](https://github.com/Uberi/speech_recognition)
 - [PyUserInput](https://github.com/SavinaRoja/PyUserInput)
 - [pytssx3](https://github.com/nateshmbhat/pyttsx3)
 - [textblob](https://github.com/sloria/TextBlob)
 - [pygame](https://github.com/pygame/)
