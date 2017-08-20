#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""utils.py: Fonctions utiles."""

import functools
import timeit
import os

class Directory_commands(object):

    def __init__(self):
        """Initialisation des variables.
        """

        self.current_directory = os.path.dirname(os.path.realpath(__file__))

    def check_directory_exist(self, dir_name):
        """Vérifie que le répertoire "name" est un sous-répertoire de l'emplacement actuel du programme.
        Args:
            dir_name (str): Nom du répertoire.
        """

        if not os.path.exists(self.current_directory + dir_name):
            os.makedirs(self.current_directory + dir_name)

    def remove_all_directory(self, dir_name, end=".png"):
        """Remove all the files in a directory.
        Args:
            dir_name (str): Nom du répertoire.
        """

        os.chdir(self.current_directory + dir_name)
        filelist = [f for f in os.listdir(".") if f.endswith(end)]
        for f in filelist: os.remove(f)
        os.chdir(self.current_directory)

def while_true(func):
    """ Décore la fonction d'une boucle while True pour les inputs.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                res = func(*args, **kwargs)
                if res == 'verif':
                    continue
                break
            except ValueError as VE:
                print(VE)
        return res
    return wrapper

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

def comp_ele_list(lst):
    return not lst or lst.count(lst[0]) == len(lst)
