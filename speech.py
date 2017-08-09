# -*- coding: utf-8 -*-
from pymouse import PyMouse
import speech_recognition as sr
import time
import os

mouse = PyMouse()
commands_list = ['demain', 'hello', 'next']
order = []

if os.path.exists("speech_coord.txt"):
    with open("speech_coord.txt", 'r') as f:
        data = f.read()
    config_list = [line.split() for line in data.splitlines()]

print(config_list)

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        callback.sample = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + callback.sample)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Déplacement de la souris
    if callback.sample == 'next':
        mouse.move(1269,419)
        mouse.click(1269,419)
        callback.sample = ''
    if callback.sample == 'stop':
        callback.exit = True

callback.sample = ''
callback.exit = False
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    print("Say something!")

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
#for _ in range(100): time.sleep(0.1)  # we're still listening even though the main thread is doing other things
#stop_listening()  # calling this function requests that the background listener stop listening

print(mouse.position())

while callback.exit == False: time.sleep(0.1)

# Write on a file
#with open("microphone-results.wav", "wb") as f:
#    f.write(audio.get_wav_data())
