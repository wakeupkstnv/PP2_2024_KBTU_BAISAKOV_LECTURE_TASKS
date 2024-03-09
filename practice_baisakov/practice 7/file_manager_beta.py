'''
/ᐠ - ˕ -マ 

ฅ/ᐠ˶> ﻌ<˶ᐟ\ฅ

/ᐠ. ｡.ᐟ\ᵐᵉᵒʷˎˊ˗

₍ᐢ._.ᐢ₎♡ ༘

'''

import os
import colorama
from msvcrt import getch

activeItemIndex = 0
currentItemIndex = 0
EnterItemIndex = None

main_path = os.getcwd()
max_point = None

def control(path) -> None:
    global activeItemIndex, control_check, max_point, EnterItemIndex, main_path
    
    draw_layer(path)
    key = ord(getch())
    
    if key == 27: #ESC
        control_check = False 
                   
    elif key == 80: #Down arrow
        activeItemIndex += 1
        if max_point == activeItemIndex:
            activeItemIndex = 0     
                          
    elif key == 72: #Up arrow
        activeItemIndex -= 1
        if activeItemIndex < 0: activeItemIndex = 0
    
    elif key == 13: #Enter
        EnterItemIndex = True
    
    elif key == 8: #bcksp
        os.chdir('..')
        main_path = os.getcwd()
        activeItemIndex = 0
        max_point = None
        os.system('cls')
        control(main_path)


def draw_layer(path: str) -> None:
    global activeItemIndex, currentItemIndex, max_point, EnterItemIndex, main_path
    currentItemIndex = 0 
    
    sorting = True # for future
    
    with os.scandir(path) as it:
        for file in it:
            if file.is_dir():
                size = len(str(file.name))
   
                if activeItemIndex == currentItemIndex:
                    if EnterItemIndex:
                        os.chdir(str(file.name))
                        main_path = os.getcwd()
                        currentItemIndex, activeItemIndex = 0, 0
                        max_point, EnterItemIndex = None, None
                        control(main_path)
                        
                    print(colorama.Back.BLUE + file.name, end=f'{' ' * (30 - size)}')
                else:
                    print(colorama.Back.WHITE + file.name, end=f'{' ' * (30 - size)}')
                currentItemIndex += 1
                print(colorama.Back.RESET)
                       
    
    with os.scandir(path) as it:            
        for file in it:
            if not file.is_dir():
                size = len(str(file.name))

                if activeItemIndex == currentItemIndex:
                    print(colorama.Back.BLUE + file.name, end=f'{' ' * (30 - size)}')
                    if EnterItemIndex:
                        os.system(str(file.name))
                        EnterItemIndex = False
                        
                else:
                    print(colorama.Back.WHITE + file.name, end=f'{' ' * (30 - size)}')
                currentItemIndex += 1
                print(colorama.Back.RESET)
        
        if max_point == None:
            max_point = currentItemIndex

        
                  
def main() -> None:
    global control_check, EnterItemIndex, main_path
    control_check = True

    while(control_check):
        os.system('cls')
        control(main_path)
 
        
if __name__ in '__main__':
    main()