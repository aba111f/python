def even_ns(n):
    for i in range(0, n):
        if i%2 == 0:
            yield i

print(list(even_ns(5)))
print(list(even_ns(15)))
print(list(even_ns(29)))