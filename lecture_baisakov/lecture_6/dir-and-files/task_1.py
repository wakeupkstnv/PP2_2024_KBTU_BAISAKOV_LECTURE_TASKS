import os

path = os.getcwd()

with os.scandir(path) as it:
    print('dir:')
    for files in it:
        if files.is_dir():
            print(' ', files.name)
            
with os.scandir(path) as it:
    print('files: ')
    for files in it:
        if not files.is_dir():
            print(' ', files.name)
    