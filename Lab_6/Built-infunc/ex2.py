def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print(u,l)

s = input()
print(up_low(s))