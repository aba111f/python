import re
str = input()
pattern = r'[a-z]\_'
x = bool(re.search(pattern,str))
print(x)
