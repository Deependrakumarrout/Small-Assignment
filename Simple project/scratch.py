#A even and odd number
'''num1=int(input("Enter a number:"))
if num1 % 2:
    print(num1,"its a odd")
else:
    print(num1,"its a even number") '''

'''num1=int(input("Enter a number:"))
if num1 >1:
    for var in range(2,num1):
        if (num1 % var)==0:
            print(num1,"its a prime number")
            break
    else:
        print(num1,"its not a prime number")

else:
    print("its not a prime number")'''

#This is word we will how find a prime number in python




#Guessing game
'''password="sucess"
guess=""
limit=3
start=1
end_of_guess=False

while password != guess and not end_of_guess:
    if start <= limit:
        guess=input("Enter your password:")
        start+=1
    else:
        end_of_guess=True

if end_of_guess:
    print("please try again later")
else:
    print("Logging you in..")'''


#Creating a translator
'''def convert(data):
    word=""
    for sence in data:
        if sence in "WingIwNG":
            word=word+ ' Deeapk '
        else:
            word=word+sence
    return word
print(convert(input("Enter a word to get convet:")))'''




#Tables in two from---
'''lan=1
var=int(input("Enter a number:"))
while lan<=10:
    print(var,"x",lan,'=',var*lan)
    lan+=1


var=int(input("Enter a number:"))
for i in range(1,11):
    print(var, "x", i, '=', var * i)'''

'''num=[
    [34,34,23],
    [53,75,34],
    [34,57,78]
]

for col in num:
    for row in col:
        print(row)'''



'''num1=[
    [15,25,45],
    [55,75,85],
    [95,15,35]
]

num2=[
    [233,645,346],
    [462,732,644],
    [456,783,567]
]
num3=[
    [864,375,722],
    [365,755,245],
    [534,632,753]
]

var=[
    [000,000,000],
    [000,000,000],
    [000,000,000]
]

for x in range(len(num1)): #we are giving the length to count each number in num1.
    for y in range(len(num1[0])):#Here we are cheaking the length of number to be count the position value
        var[x][y]=num1[x][y]+num2[x][y]+num3[x][y]  # Now giving a variable which is allready mention to store the value
                                                    # and implementing the position the x is the len of the num1 and the
                                                    # y in the position of the num1 and by that we are cheaking the value
                                                    # one by one and and after that we are making sum of the all the variable
                                                    # which are the value and then making a for again to make sum of them.
for i in var:
    print(i)'''






#To find a  decimal to  binary conversion we have to make a fuction so that with in that fuction we will write a parameter
#to take inside of our code.. Them after that we have to make a if else statement to cheak wheather prime or not...
#Then we will convert it by calling the function deciaml and by dividing with 2 and then we have to print in the num%2 division
#by 2 then input of the user and then calling the function with the parameter.

'''def decimal(num):
    if num:
        decimal(num//2)
        print(num%2)

num=int(input("Enter a number:"))
decimal(num)'''



#Here i am not using any len function without lenght fuction i am calculating the string
'''while True:
    count=0
    let=input("Enter a some string to count the value:")

    for i in let:
        count=count+1


    print("The sum of the string that the user has input is:",count)


    answer=input("Run Again? type(yes/no):")
    if answer == "yes".lower():
        continue
    elif answer == "no".lower():
        print("Don't want ot run..")
    else:
        print("invalid input")


    break'''

#
# num1=float(input("Enter a number:"))
# operator=input("Enter an operator:")
# num2=float(input("Enter another number:"))
#
# if operator=='+':
#     print(num1+num2)
# elif operator=='-':
#     print(num1+num2)
# elif operator=='*':
#     print(num1*num2)
# elif operator=='/':
#     print(num1/num2)
# else:
#     print("You have type a invalid number or operator...")



import pygame
import time
#Tried
# pygame.mixer.init()
# music=pygame.mixer.music.load("D:/music/[Songs.PK] 01 - Apnaa Mujhe Tu Lagaa.mp3")
# mixer.music.play(8)

def getdate():
    import datetime
    return datetime.datetime.now()

#if this much will be the time then the song will get executed


from pygame import mixer
# def drink_water(file,stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play(-1)
#     while True:
#         a=input()
#         if a==stopper:
#             mixer.music.stop()
#             break
#     with open ("water mp3.txt","a")as d:
#         d.write(str([str(getdate())]) + a + "\n")
#         d.close()
# if __name__ == '__main__':
#     drink_water("C:/Users/user/Downloads/water.mp3","Drank")
#
#
# def eyes(file,stopper):
#     mixer.music.load(file)
#     mixer.music.play(-1)
#     while True:
#         b=input("Write stop:")
#         if b==stopper:
#             mixer.music.stop()
#             break
#     with open("eyes mp3.txt", "a")as ad:
#         ad.write(str([str(getdate())]) + b + "\n")
#         ad.close()
# if __name__ == '__main__':
#     eyes("C:/Users/user/Downloads/eyes.mp3","stop")

#C:/Users/user/AppData/Local/Programs/Python/Python37/python.exe:

'''
from pygame import mixer
from datetime import datetime
from time import time

def loop(file,to_stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        user_input=input()
        if user_input==to_stop:
            mixer.music.stop()
            break

def log_file(text):
    with open("all in one.txt","a") as d:
        d.write(f"{text} {datetime.now()} \n")

init_water=time()
init_eyes=time()
init_exercise=time()

water=25*60
eyes=30*60
exercise=45*60

if __name__ == '__main__':
    while True:
        if time()-init_water>water:
            print("Sir this is your water time: Enter 'drank' to stop")
            loop("C:/Users/user/Downloads/water.mp3","drank")
            init_water=time()
            log_file("Dear your water drinking routine:")

        if time() - init_exercise > exercise:
            print("Sir this is your physical activity time: Enter 'done' to stop")
            loop("D:/music/[Songs.PK] 02 - Highway - Maahi Ve.mp3", "done")
            init_exercise = time()
            log_file("Dear your physical activity routine:")

        if time() - init_eyes > eyes:
            print("Sir this is your eyes exercise time:'Enter done to stop'")
            loop("C:/Users/user/Downloads/eyes.mp3", "done")
            init_eyes = time()
            log_file("Dear your eyes exercise routine:")

'''



#Program of other
import time
import pygame


# Music did not played hence I have printed it as well.
def playMusic(file):
    print(file)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def IsOfficeTime(currenttime):
    if currenttime > '09:00:00' and currenttime < '17:00:01':
        return True
    else:
        return False


NumberofWaterRemaining = 18

WaterAfterEvery = 1200  # Seconds  - 20 minutes
EyeExerciseAfterEvery = 1800  # Seconds - 30 minutes
PhysicalExerciseAfterEvery = 2700  # Seconds  - 45 minutes

waterMp3 = 'water.mp3'
eyesMp3 = 'eyes.mp3'
PhysicalMp3 = 'physical.mp3'

currenttime = time.strftime('%H:%M:%S')
WaterTakenAt = time.time()
EyeExerciseAt = time.time()
PhysicalExerciseAt = time.time()

SleepTime = 60  # Sleep time in seconds It will check after every 60 seconds.

while (IsOfficeTime(currenttime)):
    #     Check for water
    if NumberofWaterRemaining > 0:
        if (time.time() - WaterTakenAt) > WaterAfterEvery:  # water after every 20 minutes
            print("Time to drink water")
            while True:
                playMusic(waterMp3)
                if input("Enter Done if you had water: ").lower() == "done":
                    WaterTakenAt = time.time()
                    NumberofWaterRemaining -= 1
                    break
        if time.time() - EyeExerciseAt > EyeExerciseAfterEvery:
            print("Time to do eye exercise")
            while True:
                playMusic(eyesMp3)
                if input("Enter Done if you done eye exercise : ").lower() == "done":
                    EyeExerciseAt = time.time()
                    break
        if time.time() - PhysicalExerciseAt > PhysicalExerciseAfterEvery:
            print("Time to do Physical exercise")
            while True:
                playMusic(PhysicalMp3)
                if input("Enter Done if you done Physical exercise : ").lower() == "done":
                    PhysicalExerciseAt = time.time()
                    break

    time.sleep(SleepTime)
    currenttime = time.strftime('%H:%M:%S')


#Another program of a coder

import datetime
import time
import pygame


def clean_eye():
    global initial_eyes
    file = "eyes.mp3"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play(-1)
    inp = ""
    while inp != "eydone":
        inp = input("Write EyDone")
        inp = inp.lower()
        if inp != "eydone":
            print("Invalid Input. Try Again!!")
    initial_eyes = time.time()
    sound.stop()
    with open("eyes.txt", "a") as fe:
        fe.write(f"{datetime.datetime.now()} Cleaned your eyes\n")


def physical_exer():
    global initial_physical
    file = "physical.mp3"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play(-1)
    inp = ""
    while inp != "pydone":
        inp = input("Write PyDone")
        inp = inp.lower()
        if inp != "pydone":
            print("Invalid Input. Try Again!!")
    initial_physical = time.time()
    sound.stop()
    with open("physical.txt", "a") as fp:
        fp.write(f"{datetime.datetime.now()} Did Phsyical Exercise\n")

def drink_water():
    global initial_water
    file = "water.mp3"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
    sound.play(-1)
    inp = ""
    while inp != "waterdone":
        inp = input("Write waterDone")
        inp = inp.lower()
        if inp != "waterdone":
            print("Invalid Input. Try Again!!")
    initial_water = time.time()
    sound.stop()
    with open("water.txt", "a") as fw:
        fw.write(f"{datetime.datetime.now()} Drank Water\n")


check = 1
temp = 1

while True:
    date = datetime.datetime.now()
    if datetime.datetime.now().strftime("%H:%M:%S") == "9:00:00":
        initial_water = time.time()
        initial_eyes = time.time()
        initial_physical = time.time()
        check = 0

    if check == 1:
        print("Tasks (Water, Eyes Clean & Physical Exercise) will start automatically during office time (9AM to 5PM)")
        check = 0
    try:
        if date.hour >= 11 and date.hour <= 17:
            final_water = time.time()
            final_eyes = time.time()
            final_physical = time.time()
            if final_eyes - initial_eyes >= 30 * 60:
                clean_eye()
            if final_physical - initial_physical >= 45 * 60:
                physical_exer()
            if final_water - initial_water >= 25 * 60:
                drink_water()
    except:
        if temp == 1:
            print("Tasks will start from tomorrow automatically. You Can't run the programme after 9AM and before 5PM")
            temp = 0


#Another person code

###############################  Healthy Programmer ##################################


#from pygame import mixer
#from datetime import datetime

WaterMp3 = 'water.mp3'
eyesMp3 = 'eyes.mp3'
physicalMp3 = 'physical.mp3'
Number_of_glasses_remaining = 18
WaterInterval = 1200
EyeExerciseInterval = 1800
PhysicalExerciseInterval = 2700
currenttime = time.strftime("%H:%M:%S")
WaterTakenAt = time.time()
EyeExerciseAt = time.time()
PhysicalExerciseAt = time.time()
SleepTime = 5
stopper = 'done'


def isOfficeTime(currenttime):
    if currenttime > '09:00:00' and currenttime < '17:01:00':
        return 1
    else:
        return 0

def playMusic(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10)

    while True:
        a = input("Press done if the job is done:")
        if a == stopper:
            mixer.music.stop()
            break
    if a == stopper:
        return 1
    else:
        return 0


def log_now(msg):
    with open("Healthy_Programmer.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if _name_ == '__main__':
    while isOfficeTime(currenttime):
        if Number_of_glasses_remaining > 0:
            try:
                if time.time() - WaterTakenAt > WaterInterval:
                    print("Time To Have Some Water!!")
                    while True:
                        r = playMusic(WaterMp3, stopper)
                        if r == 1:
                            msg = " 250 ml Of Water Was Taken At"
                            log_now(msg)
                        else:
                            log_now("Water Was Not Taken")
                        Number_of_glasses_remaining -= 1
                        WaterTakenAt = time.time()
                        break
            except Exception as e:
                time.sleep(SleepTime)
        try:
             if time.time() - EyeExerciseAt > EyeExerciseInterval:
                 print("Time To Roll Your Eyes!!")
                 while True:
                     r = playMusic(eyesMp3, stopper)
                     if r == 1:
                         msg = "Eye Exercise Was Done At"
                         log_now(msg)
                     else:
                         log_now("Eye Exercise Was Not Done")
                     EyeExerciseAt = time.time()
                     break
        except Exception as e:
                time.sleep(SleepTime)
        try:
            if time.time() - PhysicalExerciseAt > PhysicalExerciseInterval:
                print("Time To Have Some Physical Exercise!")
                while True:
                    r = playMusic(physicalMp3, stopper)
                    if r == 1:
                        msg = "Physical Exercise was Done At"
                        log_now(msg)
                    else:
                        log_now("Physical Exercise Was Not Done")
                    PhysicalExerciseAt = time.time()
                    break
        except Exception as e:
            time.sleep(SleepTime)

        currenttime = time.strftime("%H:%M:%S")

#Another person code

import datetime
import pygame

pygame.init()

# costmizable variables
water = 'water.mp3'
eyes = 'eyes.mp3'
physical = 'physical.mp3'

input_name = input("Please input your name:")

print(f"{input_name.capitalize()} welecome to the office")

file = input_name

water_alarm = 20 # minutes
eyes_alarm = 30 # minutes
physical_alarm = 45 # minutes

# non-costimizable variables
ex = True
d = datetime.datetime.now()
water_timer = d.minute + water_alarm
eyes_timer = d.minute + eyes_alarm
physical_timer = d.minute + physical_alarm

_file = open(file,'a')

print(d)
while ex!= False:
    new_d = datetime.datetime.now()

    if water_timer >= 60 or eyes_timer >= 60 or physical_timer >= 60:
        if water_timer >= 60:
            water_timer = water_timer - 60
            d = datetime.datetime.now()
            minute = d.minute

        if eyes_timer >= 60:
            eyes_timer = eyes_timer - 60
            d = datetime.datetime.now()
            minute = d.minute

        if physical_timer >= 60:
            physical_timer = physical_timer - 60
            d = datetime.datetime.now()
            minute = d.minute
    else:
        if new_d.minute == physical_timer and new_d.minute == water_timer:
            print("Drink water and then do physical",new_d)

            pygame.mixer.music.load(water)
            pygame.mixer.music.play()

            _input4 = input()

            if _input4.lower() == "drank":
                _file.write(f"Drank Water at {datetime.datetime.now()} \n \n")
                pygame.mixer.music.stop()

            pygame.mixer.music.load(physical)
            pygame.mixer.music.play()

            _input5 = input()
            if _input5.lower() == "pydone":
                pygame.mixer.music.stop()
                _file.write(f"Physical Exercise done at {datetime.datetime.now()} \n \n")
                d = datetime.datetime.now()
                eyes_timer = d.minute + eyes_alarm
                water_timer = d.minute + water_alarm
                physical_timer = d.minute + physical_alarm


        elif new_d.minute == physical_timer and new_d.minute == eyes_timer:
            print("First do eyes exercise and then do physical")

            pygame.mixer.music.load(water)
            pygame.mixer.music.play()

            _input6 = input()

            if _input6.lower() == "eydone":
                _file.write(f"Eye Exercise done at {datetime.datetime.now()} \n \n ")
                pygame.mixer.music.stop()

            pygame.mixer.music.load(physical)
            pygame.mixer.music.play()

            _input7 = input()
            if _input7.lower() == "pydone":
                pygame.mixer.music.stop()
                _file.write(f"Physical Exercise done at {datetime.datetime.now()} \n \n")

                d = datetime.datetime.now()
                eyes_timer = d.minute + eyes_alarm
                water_timer = d.minute + water_alarm
                physical_timer = d.minute + physical_alarm



        elif new_d.minute == water_timer and new_d.minute == eyes_timer:
            print("Drink water and then do eyes exercise")

            pygame.mixer.music.load(water)
            pygame.mixer.music.play()

            _input8 = input()

            if _input8.lower() == "eydone":
                _file.write(f"Eye Exercise done at {datetime.datetime.now()} \n \n")
                pygame.mixer.music.stop()

            pygame.mixer.music.load(physical)
            pygame.mixer.music.play()

            _input9 = input()
            if _input9.lower() == "drank":
                pygame.mixer.music.stop()
                _file.write(f"Drank Water at {datetime.datetime.now()} \n \n ")
                d = datetime.datetime.now()
                eyes_timer = d.minute + eyes_alarm
                water_timer = d.minute + water_alarm
                physical_timer = d.minute + physical_alarm

        elif new_d.minute == water_timer:
            print("Please drank water",new_d)
            pygame.mixer.music.load(water)
            pygame.mixer.music.play()

            _input = input()

            if _input.lower() == "drank":
                pygame.mixer.music.stop()
                _file.write(f"Drank Water at {datetime.datetime.now()} \n \n")
                water_timer = d.minute + water_alarm

        elif new_d.minute == eyes_timer:
            print("Please do eyes exercise",new_d)
            pygame.mixer.music.load(eyes)
            pygame.mixer.music.play()

            _input2 = input()

            if _input2.lower() == "eydone":
                pygame.mixer.music.stop()
                _file.write(f"Eye Exercise done at {datetime.datetime.now()} \n \n")
                eyes_timer = d.minute + eyes_alarm

        elif new_d.minute == physical_timer:
            print("Please do physical exercise",new_d)
            pygame.mixer.music.load(physical)
            pygame.mixer.music.play()

            _input3 = input()

            if _input3.lower() == "pydone":
                pygame.mixer.music.stop()
                _file.write(f"Physical Exercise done at {datetime.datetime.now()} \n \n")
                d = datetime.datetime.now()
                eyes_timer = d.minute + eyes_alarm
                water_timer = d.minute + water_alarm
                physical_timer = d.minute + physical_alarm

_file.close()

