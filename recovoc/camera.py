#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""camera.py: Fonctions et classes d'action de la camera."""

import os

import pygame
import pygame.camera
from pykeyboard import PyKeyboard

from recovoc import utils


key = PyKeyboard()
here = os.path.abspath(os.path.dirname(__file__))

class Webcam(object):
    """Classe représentant une Webcam.

    Args:
        im_num (int): Numéro de l'image.
        vid_num (int): Numéro de la vidéo.
    """

    # Pour ne pas les écraser au réappel de la classe.
    im_num = 0
    vid_num = 0

    def __init__(self, saved=here):
        """Initialisation du module pygame.
        """

        self.dir = saved
        self.direct = utils.Directory_commands(self.dir)
        self.direct.check_directory_exist("/Snaps")
        self.direct.check_directory_exist("/Videos")
        self.direct.check_directory_exist("/Images")

        pygame.init()
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (640, 480))

    @staticmethod
    def check_cam():
        """Vérifie qu'une caméra est présente.
        """

        pygame.camera.init()
        if pygame.camera.list_cameras():
            return True

    def capture(self, new=False):
        """Screenshot format .jpeg.

        Args:
            new (boolean): Nouvelle image.
        """

        self.cam.start()
        img = self.cam.get_image()
        if not new:
            pygame.image.save(img, self.dir + "/Images/cap_default.jpg")
        else:
            pygame.image.save(img, self.dir + "/Images/cap-%03d.jpg" % Webcam.im_num)
            Webcam.im_num += 1
        self.cam.stop()

    def video(self, saved=True, new=False, period=10):
        """Vidéo non-sauvegardée.

        Args:
            new (boolean): Nouvelle video.
            saved (boolean): Sauvegarde de la video.
            period (int): Durée de la video, 10 secondes par défaut.
        """

        self.direct.remove_all_directory("/Snaps")
        self.cam.start()
        self.screen = pygame.display.set_mode((640, 480))

        self.done_capturing = False
        start_ticks = pygame.time.get_ticks()
        file_num = 0

        while not self.done_capturing:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            file_num += 1
            image = self.cam.get_image()
            self.screen.blit(image, (0,0))
            pygame.display.update()

            # Save every frame
            filename = self.dir + "/Snaps/%04d.png" % file_num
            if saved: pygame.image.save(image, filename)

            if seconds > period:
                key.tap_key(key.escape_key)
                print("Time elapse: ", seconds)
                seconds = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.done_capturing = True
        self.cam.stop()

        if saved: self.make_vid(new)

    def make_vid(self, new):
        """Cré la vidéo à partir des Images du dossier Snaps
        """

        if not new:
            os.system("ffmpeg -r 8 -f image2 -i {0}/Snaps/%04d.png -codec:v libx264 \
                      -preset medium -crf 22 -codec:a \
                      copy -loglevel quiet -y {0}/Videos/result_default.avi".format(self.dir))
        else:
            os.system("ffmpeg -r 8 -f image2 -i {1}/Snaps/%04d.png -codec:v libx264 \
                      -preset medium -crf 22 -codec:a \
                      copy -loglevel quiet -y {1}/Videos/result-{0}.avi".format(Webcam.vid_num, self.dir))
            Webcam.vid_num += 1
