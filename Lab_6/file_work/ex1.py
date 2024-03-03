import os
path = input()
directories = []
for folder in os.listdir(path):
    if os.path.isdir(os.path.join(path,folder)):
        directories.append(folder)
print(directories)
files = []
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file)):
        files.append(file)
print(files)
