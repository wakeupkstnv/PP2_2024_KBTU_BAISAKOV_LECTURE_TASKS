import os

path = ''

if os.access(path, mode=os.EX_OK):
    os.remove(path)
