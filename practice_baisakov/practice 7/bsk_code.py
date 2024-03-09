from msvcrt import getch
from colorama import Fore, Back, Style
import os 

activeItemIndex = 0

def draw_layer(path):
    global activeItemIndex
    global currentItemIndex
    currentItemIndex = 0

    with os.scandir(path) as it:
        for entry in it:
            if(entry.is_dir()):
                if activeItemIndex == currentItemIndex:
                    print(Back.GREEN + entry.name, end = '')
                else:
                    print(Back.BLACK + entry.name, end = '')
                currentItemIndex = currentItemIndex + 1
                print(Back.BLACK + '')

    with os.scandir(path) as it:
        for entry in it:
            if(not entry.is_dir()):
                if activeItemIndex == currentItemIndex:
                    print(Back.GREEN + entry.name, end = '')
                else:
                    print(Back.BLACK + entry.name, end = '')
                currentItemIndex = currentItemIndex + 1
                print(Back.BLACK + '')

    print(Style.RESET_ALL)


while True:
    os.system("cls")
    draw_layer(os.getcwd())
    key = ord(getch())
    if key == 27: #ESC
        break
    elif key == 80: #Down arrow
        activeItemIndex = activeItemIndex + 1
    elif key == 72: #Up arrow
        activeItemIndex = activeItemIndex - 1
