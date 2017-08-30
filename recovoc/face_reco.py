#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""face_reco.py: Reconnaissance faciale via le module face_recognition."""

from PIL import Image, ImageDraw
import face_recognition


class Reco_face(object):
    """Reconnaissance faciale.
    """

    def __init__(self, source="Images/cap_default.jpg"):
        """Initialisation du module.

        Kwargs:
            source (str): Emplacement de l'image par défaut.
        """

        self.source = source

    def find_face(self):
        """Trouve les personnes dans une image.
        """

        image = face_recognition.load_image_file(self.source)
        face_locations = face_recognition.face_locations(image)

        face_number = len(face_locations)
        print(face_number)

        for face_num, face_location in enumerate(face_locations):
            # Print the location of each face in this image
            top, right, bottom, left = face_location

            # You can access the actual face itself like this:
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            #pil_image.show()
            pil_image.save(self.source + "_face-{:02d}.jpg".format(face_num))

    def find_facial_features(self):
        """Find all facial features in all the faces in the image.
        """

        image = face_recognition.load_image_file(self.source)
        face_landmarks_list = face_recognition.face_landmarks(image)

        face_number = len(face_landmarks_list)

        for face_num, face_landmarks in enumerate(face_landmarks_list):

            facial_features = ['chin', 'left_eyebrow', 'right_eyebrow', 'nose_bridge',
                               'nose_tip', 'left_eye', 'right_eye', 'top_lip', 'bottom_lip']
            # Let's trace out each facial feature in the image with a line!
            pil_image = Image.fromarray(image)
            d = ImageDraw.Draw(pil_image)

            for facial_feature in facial_features:
                d.line(face_landmarks[facial_feature], width=5)

            #pil_image.show()
            pil_image.save(self.source + "_face_feature-{:02d}.jpg".format(face_num))

if __name__ == '__main__':
    r = Reco_face()
    r.find_face()
    r.find_facial_features()
