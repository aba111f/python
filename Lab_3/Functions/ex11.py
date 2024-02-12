def polindrome(word):
    if word == ''.join(reversed(word)):
        return True
    else:
        return False

print(polindrome('abc'))
print(polindrome('abba'))
print(polindrome('aba'))