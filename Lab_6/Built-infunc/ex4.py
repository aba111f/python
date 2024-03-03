import math
import time
def sqroot(n,t):
    res = math.sqrt(n)
    time.sleep(t/1000)
    print(f"Square root of {n} after {t} miliseconds is {res}")

a = int(input())
b = int(input())
print(sqroot(a,b))







    