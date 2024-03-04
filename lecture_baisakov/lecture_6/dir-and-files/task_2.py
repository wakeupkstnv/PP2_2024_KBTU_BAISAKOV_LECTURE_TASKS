import os

path = os.getcwd()

print(os.access(path, mode=os.R_OK), 
      os.access(path, mode=os.W_OK), 
      os.access(path, mode=os.X_OK),
      os.access(path, mode=os.EX_OK))

