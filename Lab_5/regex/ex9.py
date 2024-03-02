import re
str = input()
pattern = r'(\w)([A-Z])'
x = re.sub(pattern, r"\1 \2",str)
print(x)