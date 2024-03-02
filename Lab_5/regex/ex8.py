import re
str = input()
pattern = r'[a-zA-Z][^A-Z]*'
x = re.findall(pattern, str)
print(x)