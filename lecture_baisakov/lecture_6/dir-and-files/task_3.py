import os

path = os.getcwd()

if os.access(path, mode=os.EX_OK):
    for files in os.listdir(path):
        print(files)
    
    # or print(os.listdir(path))
