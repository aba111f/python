def decrease(n):
    while n != 0:
        yield n
        n = n-1

print(list(decrease(5)))