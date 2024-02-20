def even_ns(n):
    for i in range(0, n):
        if i%2 == 0:
            yield i



x = list(even_ns(5))
nums_str = ', '.join(map(str,x))
print(nums_str)