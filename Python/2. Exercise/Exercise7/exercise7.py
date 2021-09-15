# -----Healthy Programmer-----
"""
Rules -
9 am to 5 pm
Water - water.mp3 - every 40 min - Drank - log
Eyes - eyes.mp3 - every 30 min - EyDone - log
Physical activity - physical.mp3 - every 45 min - ExDone - log
use pygame module to play audio
"""
from pygame import mixer
from datetime import datetime
from time import time

# customizable variables
water = 'water.mp3'
eyes = 'eyes.mp3'
physical = 'physical.mp3'

water_alarm = 40  # minutes
eyes_alarm = 30  # minutes
physical_alarm = 45  # minutes


def music_on_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.7)
    mixer.music.play(100, 0.0)
    while True:
        query = input()
        if query == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("myLogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    user_name = input("Please input your name:")
    print(f"{user_name.capitalize()} welcome to the office.")

    init_water = time()
    init_eyes = time()
    init_exercise = time()

    while True:
        if time() - init_water > water_alarm * 60:
            print("Water drinking time. Enter 'drank' to stop the alarm.")
            music_on_loop(water, "drank")
            log_now("Drank water at:")
            init_water = time()

        if time() - init_eyes > eyes_alarm * 60:
            print("Eyes exercise time. Enter 'eydone' to stop the alarm.")
            music_on_loop(eyes, "eydone")
            log_now("Eyes relaxed at:")
            init_eyes = time()

        if time() - init_exercise > physical_alarm * 60:
            print("Physical activity time. Enter 'pydone' to stop the alarm.")
            music_on_loop(physical, "pydone")
            log_now("Physical activity done at:")
            init_exercise = time()
