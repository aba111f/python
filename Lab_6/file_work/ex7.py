import os 

text = 'C:/Users/karat/Рабочий стол/pp2/Lab_6/file_work/1.txt'
text2= 'C:/Users/karat/Рабочий стол/pp2/Lab_6/file_work/2.txt'

file = open(text)
data = file.read()
file.close()

with open(text2, 'a') as file2:
    file2.write(data)
