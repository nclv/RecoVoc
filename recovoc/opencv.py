#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

import cv2
import numpy as np
import pygame.camera #list_camera
from pykeyboard import PyKeyboard

from recovoc import utils


key = PyKeyboard()
here = os.path.abspath(os.path.dirname(__file__))

class ImageProcessing(object):
    """Classe opencv.

    Args:
        im_num (int): Numéro de l'image.
        vid_num (int): Numéro de la vidéo.
    """

    # Pour ne pas les écraser au réappel de la classe.
    im_cap_num = 0
    im_sup_num = 0
    vid_num = 0

    def __init__(self, saved=here):
        """Initialisation du module pygame.

        Kwargs:
            saved (str): Emplacement des enregistrements.
        """

        self.dir = saved
        self.direct = utils.Directory_commands(self.dir)
        self.direct.check_directory_exist("/Videos")
        self.direct.check_directory_exist("/Images")
        self.direct.check_directory_exist("/Images/Know_people")

    @staticmethod
    def check_cam():
        """Vérifie qu'une caméra est présente.
        """

        pygame.camera.init()
        if pygame.camera.list_cameras():
            return True

    def load_image(self, direct, color=1, period=0):
        """Charge l'image et l'affiche.

        Args:
            direct (str): Emplacement de l'image.

        Kwargs:
            color (int): Couleur de l'image.
            period (int): Durée d'ouverture.
        """

        # Load an color image in grayscale
        self.img = cv2.imread(direct, color) # 0,1

        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        cv2.imshow('img', self.img)
        k = cv2.waitKey(period*1000) & 0xFF
        if k == ord('q'): # pragma: no cover
            cv2.destroyAllWindows()

    def image_superpose(self, dir_im1, dir_im2, period=0):
        """Superpose 2 images.

        Args:
            dir_im1, dir_im2 (str): Emplacement des images.
            period (int): Durée d'ouverture.
        """

        img1 = cv2.imread(dir_im1)
        img2 = cv2.imread(dir_im2)
        direct = self.dir + "/Images/cap_superpose-{:03d}.jpg".format(ImageProcessing.im_sup_num)

        self.img = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        cv2.imshow('img', self.img)
        k = cv2.waitKey(period*1000) & 0xFF
        if k == ord('q'): # pragma: no cover
            cv2.destroyAllWindows()
        cv2.imwrite(direct, self.img)
        ImageProcessing.im_sup_num += 1

    def set_cam(self, cam_index, resolution):
        """Prépare la caméra.

        Args:
            cam_index (int): Index de la camera.
            resolution (list): Résolution de l'image.
        """

        self.cap = cv2.VideoCapture(cam_index)

        # Check if camera opened successfully
        if (self.cap.isOpened() == False): # pragma: no cover
            print("Error opening video stream or file")

        self.ret = self.cap.set(3, resolution[0])
        self.ret = self.cap.set(4, resolution[1])

    def image_capture(self, resolution=[1920, 1080], cam_index=0, new=False, period=10):
        """Capture une image.

        Kwargs:
            cam_index (int): Index de la camera.
            resolution (list): Résolution de l'image.
            new (bool): Nouvelle image.
            period (int): Durée d'affichage.
        """

        self.set_cam(cam_index, resolution)

        self.ret, frame = self.cap.read()

        start = time.time()
        while time.time() - start < period:
            cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
            cv2.imshow('frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'): # pragma: no cover
                break

        if new:
            cv2.imwrite(self.dir + "/Images/cap-%03d.jpg" % ImageProcessing.im_cap_num, frame)
            ImageProcessing.im_cap_num += 1
        else:
            cv2.imwrite(self.dir + "/Images/cap_default.jpg", frame)

        self.cap.release()
        cv2.destroyAllWindows()

    def video_capture(self, resolution=(1920, 1080), cam_index=0, saved=True, new=False, period=10):
        """Sauvegarde la video.

        Kwargs:
            cam_index (int): Index de la camera.
            resolution (list): Résolution de l'image.
            saved (bool): Sauvegarde.
            new (bool): Nouvelle image.
            period (int): Durée d'affichage.
        """

        self.set_cam(cam_index, resolution)

        if saved:
            # Define the codec and create VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            if not new:
                out = cv2.VideoWriter(self.dir + "/Videos/vid_default.avi", fourcc, 20.0, resolution)
            else:
                out = cv2.VideoWriter(self.dir + "/Videos/vid-{}.avi".format(ImageProcessing.vid_num), fourcc, 20.0, resolution)
                ImageProcessing.vid_num += 1

        start = time.time()
        while(self.cap.isOpened() and (time.time() - start < period)):
            ret, frame = self.cap.read()
            if ret == True:
                if saved: out.write(frame)
                cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
                cv2.imshow('frame', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'): # pragma: no cover
                    break
            else: # pragma: no cover
                break

        # Release everything if job is finished
        self.cap.release()
        if saved: out.release()
        cv2.destroyAllWindows()

    def video_play(self, direct):
        """Play a video.

        Args:
            direct (str): Emplacement de l'image.
        """

        self.cap = cv2.VideoCapture(direct)

        # Check if camera opened successfully
        if (self.cap.isOpened() == False): # pragma: no cover
            print("Error opening video stream or file")

        # Read until video is completed
        while(self.cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            if ret == True:
                cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
                # Display the resulting frame
                cv2.imshow('frame', frame)
                # Press Q on keyboard to  exit
                if cv2.waitKey(50) & 0xFF == ord('q'): # pragma: no cover
                    break
            else: # pragma: no cover
                break
        # When everything done, release the video capture object
        self.cap.release()
        # Closes all the frames
        cv2.destroyAllWindows()


if __name__ == '__main__':
    c = ImageProcessing()
    c.video_capture(saved=False)
    c.video_capture()
    c.video_capture(new=True)
    c.video_play("Videos/vid_default.avi")
    c.image_capture()
    c.image_superpose("Images/cap_default.jpg", "Images/cap-000.jpg")
