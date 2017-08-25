#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""test_camera.py: Tests du module Camera.
"""

from context import recovoc
from recovoc.camera import Webcam

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

@unittest.skipIf(Webcam.check_cam() is None, "There is no camera detected.")
class TestCamera(unittest.TestCase):
    """Camera Test class.
    """

    def setUp(self):
        self.c = Webcam(saved=here)

    def test_capture(self):
        self.c.capture()
        self.assertTrue(os.path.isfile(here + "/Images/cap_default.jpg"))

    def test_new_capture(self):
        self.c.capture(new=True)
        self.assertTrue(os.path.isfile(here + "/Images/cap-000.jpg"))

    def test_video(self):
        self.c.video(saved=True, period=5)
        self.assertTrue(os.path.isdir(here + "/Snaps"))
        self.assertTrue(os.path.isfile(here + "/Videos/result_default.avi"))

    @ignore_warnings
    def test_new_video(self):
        self.c.video(saved=True, new=True)
        self.assertTrue(os.path.isfile(here + "/Videos/result-0.avi"))

    @staticmethod
    def tearDown():
        """Remove created files and directories.
        """

        shutil.rmtree(here + "/Images")
        shutil.rmtree(here + "/Videos")
        shutil.rmtree(here + "/Snaps")

if __name__ == '__main__':
    unittest.main()
