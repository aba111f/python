import re
str = input()
pattern = r''
x = re.sub(pattern,'_',str)
print(x)