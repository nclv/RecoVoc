#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""test_camera.py: Tests du module Camera.
"""

from context import recovoc
from recovoc.opencv import ImageProcessing

import unittest
import warnings
import os
import shutil


here = os.path.abspath(os.path.dirname(__file__))

def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            test_func(self, *args, **kwargs)
    return do_test

@unittest.skipIf(ImageProcessing.check_cam() is None, "There is no camera detected.")
class TestCamera(unittest.TestCase):
    """Camera Test class.
    """

    def setUp(self):
        self.c = ImageProcessing(saved=here)

    def test_capture(self):
        self.c.image_capture(period=2)
        self.assertTrue(os.path.isfile(here + "/Images/cap_default.jpg"))
        self.c.load_image(here + "/Images/cap_default.jpg", period=2)

    def test_new_capture(self):
        self.c.image_capture(new=True, period=2)
        self.assertTrue(os.path.isfile(here + "/Images/cap-000.jpg"))

    def test_superpose(self):
        self.c.image_capture(new=True, period=1)
        self.c.image_capture(period=1)
        self.c.image_superpose(here + "/Images/cap_default.jpg", here + "/Images/cap-001.jpg", period=5)
        self.assertTrue(os.path.isfile(here + "/Images/cap_superpose-000.jpg"))

    def test_video(self):
        self.c.video_capture()
        self.assertTrue(os.path.isfile(here + "/Videos/vid_default.avi"))
        self.c.video_play(here + "/Videos/vid_default.avi")

    def test_new_video(self):
        self.c.video_capture(new=True)
        self.assertTrue(os.path.isfile(here + "/Videos/vid-0.avi"))

    @staticmethod
    def tearDown():
        """Remove created files and directories.
        """

        shutil.rmtree(here + "/Images")
        shutil.rmtree(here + "/Videos")


if __name__ == '__main__':
    unittest.main()
