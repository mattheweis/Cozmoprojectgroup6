import cozmo
import librosa
from pygame import mixer
mixer.init()
import time
import _thread
import random

canplay = 0
color = [cozmo.lights.blue_light,cozmo.lights.green_light,cozmo.lights.red_light]
def play(robot, n, tempo):
    global color
    global canplay
    global mixer
    mixer.music.load("Good/"+n+".mp3")
    mixer.music.play()
    delay = 60 / tempo
    while canplay == 1:
        ran_color = random.randint(0,2)
        print('Tick')
        robot.set_all_backpack_lights(color[ran_color])
        time.sleep(delay)
        
def cozmo_program(robot: cozmo.robot.Robot):
    global canplay
    global mixer
    while True:
        a = input("Command = ")
        if a == 'Play':
           
            n = input() 
            print('Loading...')
            x, sr= librosa.load("Good/"+n+".mp3")
            tempo, beat_times = librosa.beat.beat_track(x, sr=sr, start_bpm=60, units='time')
            print('tempo = '+str(tempo))
            canplay = 1
            _thread.start_new_thread(play , (robot, n, tempo))
        elif a == 'Stop':
            mixer.music.stop()
            canplay = 0
        elif a == 'Exit':
            break
        else:
            print('invalid command')
    print('End program')


cozmo.run_program(cozmo_program)