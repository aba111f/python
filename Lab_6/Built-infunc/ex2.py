def is_up_low(word):
    up = 0
    low = 0
    for i in word:
        if i.isupper():
            up += 1
        else:
            low += 1
    print(up, low)

word = input()
print(is_up_low(word))