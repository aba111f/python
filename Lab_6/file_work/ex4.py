import os 

filename = input()
count_lines = 0


if os.path.exists(filename):
    with open(filename) as file:
        for line in file:
            count_lines += 1
        print(count_lines)
else:
    print('file not found')