import re
str = input()
pattern = r'[ ,.]'
x = re.sub(pattern, ':',str)
print(x)