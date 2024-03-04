import os 

filename = input()

if os.path.exists(filename):
    os.remove(filename)
else:
    print("file not found")