import os

path = input()

if os.path.exists(path):
    print(os.listdir(path))
else:
    print('path not found')