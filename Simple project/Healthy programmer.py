#Healthy programmer
#Create  a program like this -
#3.5 liter of water and 15-18 200 ml k glasses of water and in every 30 min eye exercise and then every
#45 minutes you have to do some physical activities.

# Water - For water we will make a program that play water.mp3 in this directory
# Eyes - For eyes we will make eyes.mp3
# Physical activity - Physical.mp3 in this directory

#we have to write a program to 9:00am to 5:00pm within this time he will drink water
#we can use datetime module

#Using of py_game
#Using of time module
#Using of logging file
#Using of love come on..
'''
from pygame import mixer
from datetime import datetime
from time import time

def loops(file,stopper):
    mixer.init()    #mixer.init()
    mixer.music.load(file)  #mixer.music.load(file)
    mixer.music.play(-1)    #mixer.music.play(-1)
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def log(ms):
    with open ("All detail.txt","a")as d:
        d.write(f"{ms} {datetime.now()} \n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_physical_exercise = time()
    watersecs=20*60
    exsecs=30*60
    eyessecs=45*60

    while True:
        if time()-init_water>watersecs:
            print("Its your water drinking time Enter 'drank to stop the alarm.'")
            loops("C:/Users/user/Downloads/water.mp3", "drank")
            init_water=time()
            log("Drank water At:")
        if time()-init_eyes>eyessecs:
            print("Its your eyes exercise time Enter 'done to stop the alarm.'")
            loops("C:/Users/user/Downloads/eyes.mp3","done")
            init_eyes=time()
            log("Eyes Relaxed at:")
        if time() - init_physical_exercise > exsecs:
            print("Its your physical_Activity time Enter 'done to stop the alarm.'")
            loops("C:/Users/user/Downloads/eyes.mp3", "done")
            init_physical_exercise = time()
            log("Physical Activity drank at:")

            '''

'''
from pygame import mixer
from datetime import datetime
from time import time

def loop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        user_input=input()
        if user_input==stopper:
            mixer.music.stop()
            break
def log(msg):
    with open("Detail.txt","a") as op:
        op.write(f"{msg} {datetime.now()} \n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    water = 10
    eyes = 20
    exercise = 40

    while True:
        if time()-init_water>water:
            print("Sir this is your drinking water time Enter 'drank' to stop")
            loop("C:/Users/user/Downloads/water.mp3","drank")
            init_water=time()
            log("Sir in this time you have drank water this:")
        if time()-init_eyes>eyes:
            print("Sir this is your eyes exercise Enter 'done' to stop")
            loop("C:/Users/user/Downloads/eyes.mp3","done")
            init_eyes=time()
            log("Sir in this time you have done eyes exercise this:")
        if time()-init_exercise>exercise:
            print("Sir this is your physical activity time Enter 'done' to stop")
            loop("D:/music/barfi (3).mp3","done")
            init_exercise=time()
            log("Sir in this time you have done physical activity this:")
'''


#Uplord on github
from pygame import mixer
from datetime import datetime
from time import time

init_water = time()
init_eye_exercise = time()
init_physical_exercise = time()

drink_water = 20*60
eye_exercise = 30*60
physical_exercise = 45*60

while True:
    if time() - init_water > drink_water:
        print("Its time to drink water [Enter drank to stop]:")
        mixer.init()
        mixer.music.load("C:/Users/user/Downloads/water.mp3")
        mixer.music.play(-1)
        with open("Time table", "a") as id:
            id.write("This is your drinking water detail: " + str(datetime.now()) + "\n")
        id.close()
        user_input = input()

        while True:
            if user_input != "drank":
                print("Please insert the correct word:")
                mixer.music.load("C:/Users/user/Downloads/water.mp3")

            if user_input == "drank":
                mixer.music.stop()
                init_water = time()
            break

    if time() - init_eye_exercise > eye_exercise:
        print("Sir its time to do eye exercise [Enter done to stop]:")
        mixer.init()
        mixer.music.load("C:/Users/user/Downloads/eyes.mp3")
        mixer.music.play(-1)
        with open("Time table","a") as id:
            id.write("Sir this is your eyes exercise schedule:"+str(datetime.now())+"\n")
        id.close()
        user_input =  input()

        while True:
            if  user_input != "done":
                print("Please insert the correct word:")
                mixer.music.load("C:/Users/user/Downloads/eyes.mp3")

            if user_input == "done":
                mixer.music.stop()
                init_eye_exercise = time()
            break

    if time() - init_physical_exercise > physical_exercise:
        print("Its time to so some physical activity: [Enter done to stop]")
        mixer.init()
        mixer.music.load("D:/music/05 - Jackpot - Kabhi Jo Baadal Barse (Remix By Maxi) [DJMaza.Info].mp3")
        mixer.music.play(-1)
        with open("Time table","a") as id:
            id.write("This is your schedule of physical activity:"+str(datetime.now())+"\n")
        id.close()
        user_input = input()

        while True:
            if user_input != "done":
                print("Please enter the correct word:")
                mixer.music.load("D:/music/05 - Jackpot - Kabhi Jo Baadal Barse (Remix By Maxi) [DJMaza.Info].mp3")
            if user_input == "done":
                mixer.music.stop()
                init_physical_exercise = time()
            break








