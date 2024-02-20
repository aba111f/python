def squares(a, b):
    for i in range(a, b):
        yield i**2

print(list(squares(1, 9)))
print(list(squares(10, 15)))
print(list(squares(6, 9)))