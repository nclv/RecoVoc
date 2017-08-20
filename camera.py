#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""camera.py: Fonctions et classes d'action de la camera."""

import functools
import time
import sys
import os

import pygame
import pygame.camera

import utils


class Webcam(object):
    """Classe représentant une Webcam.

    Args:
        im_num (int): Numéro de l'image.
        vid_num (int): Numéro de la vidéo.
    """

    # Pour ne pas les écraser au réappel de la classe.
    im_num = 0
    vid_num = 0

    def __init__(self):
        """Initialisation du module pygame.
        """

        self.direct = utils.Directory_commands()
        self.direct.check_directory_exist("/Snaps")
        self.direct.check_directory_exist("/Videos")
        self.direct.check_directory_exist("/Images")

        self.source = "/dev/video0"

        pygame.init()
        pygame.camera.init()

        self.infoObject = pygame.display.Info()
        # Taille de l'écran
        #self.cam = pygame.camera.Camera(self.source, (self.infoObject.current_w, self.infoObject.current_h))
        self.cam = pygame.camera.Camera(self.source, (640, 480))

    def capture(self, new=False):
        """Screenshot format .jpeg.
        """

        self.cam.start()
        img = self.cam.get_image()
        if not new:
            pygame.image.save(img, "Images/cap_default.jpg")
        else:
            pygame.image.save(img, "Images/cap-%03d.jpg" % Webcam.im_num)
            Webcam.im_num += 1
        self.cam.stop()

    def unsaved_video(self):
        """Vidéo non-sauvegardée.
        """

        self.direct.remove_all_directory("/Snaps")
        self.cam.start()
        self.screen = pygame.display.set_mode((640, 480))

        self.done_capturing = False
        while not self.done_capturing:
            image = self.cam.get_image()
            self.screen.blit(image, (0,0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done_capturing = True
        self.cam.stop()

    def saved_video(self, new=False):
        """Vidéo sauvegardée.
        """

        self.direct.remove_all_directory("/Snaps")
        self.cam.start()
        self.screen = pygame.display.set_mode((640, 480))

        self.done_capturing = False
        file_num = 0

        while not self.done_capturing:
            file_num = file_num + 1
            image = self.cam.get_image()
            self.screen.blit(image, (0,0))
            pygame.display.update()

            # Save every frame
            filename = "Snaps/%04d.png" % file_num
            pygame.image.save(image, filename)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done_capturing = True
        self.cam.stop()

        if not new:
            os.system("ffmpeg -r 8 -f image2 -i Snaps/%04d.png -codec:v libx264 -preset medium -crf 22 -codec:a copy -y Videos/result_default.avi")
        else:
            os.system("ffmpeg -r 8 -f image2 -i Snaps/%04d.png -codec:v libx264 -preset medium -crf 22 -codec:a copy -y Videos/result-{}.avi".format(Webcam.vid_num))
            Webcam.vid_num += 1

if __name__ == '__main__':
    # Tests
    c = Webcam()
    c.capture()
    c.capture(new=True)
    c.unsaved_video()
    c.saved_video()
    c.saved_video(new=True)
    c.saved_video(new=True)
