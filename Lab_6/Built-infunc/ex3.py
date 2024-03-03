def polyndrome(word):
    word = word.lower()
    rev = ''.join(reversed(word))
    if word == rev:
        print('the word is polyndrome')
    else:
        print('false')

word = input()
print(polyndrome(word))