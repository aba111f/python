import re
str = input()
pattern = r'ab*'
x = bool(re.search(pattern,str))
print(x)
