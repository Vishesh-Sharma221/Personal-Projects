from time import time
from datetime import datetime
from pygame import mixer 
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        a = input()
        if a == stopper:
            mixer.music.stop
            print("Saved it !")
            talk("Saved it !")
            break

def addlogs(msg):
    with open('logs.txt','a') as f:
        f.write(f"{msg} at {datetime.now()}\n")
    

if __name__ == '__main__':
    print("Health Program started!")
    talk("Health Program started!")
# Initialising time for water break, eyes and physical exercise 

    init_water = time()
    init_eyes = time()
    init_exc = time()

#  Declaring variables to set how much time interval we need for the breaks

    talk("I will remind you to drink water after every?")
    water_time = int(input("\nI will remind you to drink water after every? (minute) : "))*60
    talk("I will remind you to relax eyes after every?")
    eyes_time = int(input("\nI will remind you to relax eyes after every? (minute) : "))*60
    talk("I will remind you to do physical exercise after every?")
    exc_time = int(input("\nI will remind you to do physical exercise after every? (minute) : "))*60

    talk("All set! Leave me in the background and continue your work")
    print("\n All set! Leave me in the background and continue your work :D")

# Now just running the while loop using all the variables and functions we created 

    while True:
        if time() - init_water > water_time:
            print("Water Break sir! Type 'drank' to let me know you are done!\n")
            musiconloop("water.WAV","drank")
            init_water = time()
            addlogs("Drank Water")

        if time() - init_eyes > eyes_time:
            print("Eyes Break sir! Type 'done' to let me know you are done!\n")
            musiconloop("eyes.WAV","done")
            init_eyes = time()
            addlogs("Did eyes exercise")

        if time() - init_exc > exc_time:
            print("Take Break sir! Type 'done exercise' to let me know you are done!\n")
            musiconloop("physical.WAV","exercise done")
            init_exc = time()
            addlogs("Did physical exercise")

# ------------------------CODE ENDS HERE -----------------------------------------