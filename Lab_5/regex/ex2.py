import re
str = input()
pattern = r'ab{2,3}'
x = bool(re.search(pattern,str))
print(x)
