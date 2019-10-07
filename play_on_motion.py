import pygame
import sys
import os
from gpiozero import MotionSensor
from time import sleep
from random import choice
from datetime import datetime

SOUNDS_PATH = sys.argv[1]
FORCED_WAIT_TIME = float(sys.argv[2]) #seconds, so rn, 1 hour

_,_, sound_files = os.walk(SOUNDS_PATH).next()

def play_sound(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

pir = MotionSensor(4)
while True:
    next_sound_path = os.sep.join([SOUNDS_PATH,choice(sound_files)])
    print "Waiting for motion..."
    pir.wait_for_motion()
    print "Playing",next_sound_path
    print datetime.now()
    play_sound(next_sound_path)
    print "Forced wait in progress..."
    sleep(FORCED_WAIT_TIME)

