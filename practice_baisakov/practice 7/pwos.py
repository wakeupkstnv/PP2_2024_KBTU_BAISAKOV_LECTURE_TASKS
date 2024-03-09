import os
import colorama
from colorama import Fore
from random import randint

path = os.getcwd()
all_color = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.CYAN, Fore.LIGHTMAGENTA_EX]
def check_dirs(path: str) -> None:
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                print(all_color[randint(0, 4)] + entry.name)

    print(colorama.Fore.RESET, end='') 

check_dirs(path)        
  
            

