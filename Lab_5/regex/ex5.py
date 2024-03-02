import re
str = input()
pattern = r'a.*b$'
x = bool(re.search(pattern,str))
print(x)
