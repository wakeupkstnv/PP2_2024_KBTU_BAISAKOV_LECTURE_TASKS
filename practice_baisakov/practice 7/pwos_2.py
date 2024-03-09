import os
import colorama
from msvcrt import getch

count = 0

while True:
    
    key = ord(getch())
    print(key)
    if key == 27:
        os.system('cls')
        break
    
    if key == 72:
        os.system('cls')
        count += 1
        print('count up!')
        print(count)

    if key == 80:
        os.system('cls')
        count -= 1
        print('count down!')
        print(count)
    
        


    
 

