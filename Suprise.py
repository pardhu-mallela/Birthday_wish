import os, random, pyttsx3, sys
from threading import Thread
from time import sleep
from love import code

from termcolor import colored
# from playsound import playsound
import pygame

from config import *


# Importing module specified in the config file
art = __import__(f'arts.{artFile}', globals(), locals(), ['*'])


def replaceMultiple(mainString, toBeReplace, newString):
    """
    [Replace a set of multiple sub strings with a new string]
    Args:
        mainString ([string]): [String in which the replacement will be done]
        toBeReplace ([list]): [A list which elements will be replaced by a newString]
        newString ([string]): [A string which will be replaced in place of elements of toBeReplace]
    Returns:
        [string]: [Return the main string where the element of toBeReplace is replaced by newString]
    """

    # Iterate over the list to be replaced
    for elem in toBeReplace:
        # Check if the element is in the main string
        if elem in mainString:
            # Replace the string
            mainString = mainString.replace(elem, newString)

    return mainString


def pprint(art, time):
    color_used = [random.choice(color)]
    colorAttribute = []
    for i in range(len(art)):
        if art[i] in colorCodes:
            # Color attr set to blink if 9
            if art[i] == '⑨':
                colorAttribute = [colorCodes[art[i]]]
            # color attr none if 10
            elif art[i] == '⑩':
                colorAttribute = []
            # Random color if R
            elif art[i] == '®':
                color_used = color
            else:
                color_used = [colorCodes[art[i]]]

        print(colored(replaceMultiple(art[i], colorCodes, ''), random.choice(color_used), attrs=colorAttribute), sep='',
              end='', flush=True)
        sleep(time)


def pAudio():
    if playAudio:
        # playsound(audio)
        pygame.mixer.init()
        pygame.mixer.music.load(audio)
        pygame.mixer.music.play()

        # Keep the program running while the music is playing
        while pygame.mixer.music.get_busy():
            sleep(1)


def pcode():
    # Print the code before wishing
    if codePrint:
        for i in range(len(art.code)):
            print(colored(art.code[i], codeColor), sep='', end='', flush=True)
            sleep(codingSpeed)
        input('\n\n' + colored('python3', 'blue') + colored(' Suprise.py', 'yellow'))
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        input(colored('press {Enter}...', 'blue'))
        os.system('cls' if os.name == 'nt' else 'clear')


# Clearing terminal
os.system('cls' if os.name == 'nt' else 'clear')
pcode()
obj1 = Thread(target=pAudio)
obj2 = Thread(target=pprint, args=(art.mainArt, speed))
# sleep(82)
# choice = input(colored("Enter k : ", 'green'))

obj1.start()
obj2.start()

obj1.join()
obj2.join()

msg = '''
Hii Ramya... Wish you many more happy returns of the day....
I don't know what to say now..........
I don't know much about you. I don't know your likes and dislikes. I even don't know that 
        you like these kind of wishes or not. I guess many people wishes you in many innovative ways. 
        I thought a lot about how to wish you a happy birthday. I can't come to your house and give you surprise...

So I want to wish you in a different way. I hope you like this.......
Happy Birthday my dear. I wish you should be one of the most happiest persons in the world. 
        Don't forget, I always remember my words and promise...
'''


def message():
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 1)

    def speak(x):
        engine.say(x)
        engine.runAndWait()

    engine.save_to_file(msg, "voice.mp3")
    sleep(1)
    speak('''Hii Ramya... Wish you many more happy returns of the day.''')
    sleep(0.5)

    speak("I don't know what to say now...")
    sleep(0.9)

    speak('''I don't know much about you. I don't know your likes and dislikes. I even don't know that 
        you like these kind of wishes or not. I guess many people wishes you in many innovative ways. 
        I thought a lot about how to wish you a happy birthday. I can't come to your house and give you surprise.
        ''')
    sleep(0.5)

    speak('So I want to wish you in a different way. I hope you like this.')
    sleep(0.4)

    speak('''Happy Birthday my dear. I wish you should be one of the most happiest persons in the world. 
        Don't forget, I always remember my words and promise''')
    sleep(0.1)

    # speak("One window icon will display on your taskbar after the countdown, click on that.")
    # sleep(0.1)


def letter_by_letter():
    i = 0.1

    def write(msg):
        for char in msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(i)
    sleep(1)
    write('''Hii Ramya... ''')
    sleep(0.4)

    i = 0.05
    write('''Wish you many more happy returns of the day.\n''')
    sleep(0.5)

    i = 0.1
    write("I don't know what to say now...\n")
    sleep(0.9)

    i = 0.07
    write('''I don't know much about you. I don't know your likes and dislikes. I even don't know that you like these kind of wishes or not. 
I guess many people wishes you in many innovative ways. 
I thought a lot about how to wish you a happy birthday. \nI can't come to your house and give you suprise.
''')
    sleep(0.5)

    write('So I want to wish you in a different way. I hope you like this.')
    sleep(0.4)

    write('''\nHappy Birthday my dear. I wish you should be one of the most happiest persons in the world.
Don't forget, I always remember my words and promise.''')
    sleep(0.1)
    # write("\nOne window icon will display on your taskbar after the countdown, click on that.")
    # sleep(0.1)


msg_obj = Thread(target=message)
text_obj = Thread(target=letter_by_letter)
msg_obj.start()
text_obj.start()

msg_obj.join()
text_obj.join()

# countdown

print("\n")

# for i in range(5, -1, -1):
#     if i == 0:
#         print(i)
#     else:
#         print(str(i) + '...', end=' ')
#         sleep(1)
#
#
# print("\nClick Now")
sleep(0.9)
# GUI Turtle Graphics
code()
