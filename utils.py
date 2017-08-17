#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""utils.py: Fonctions utiles."""

import functools
import timeit

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
