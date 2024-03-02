import re
str = input()
pattern = r'^[A-Z]{1},+[a-z]'
x = bool(re.search(pattern,str))
print(x)
