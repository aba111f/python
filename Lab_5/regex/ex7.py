import re
str = input()
pattern = r'[_]'
x = re.sub(pattern, '',str)
print(x)