import random 
print('Hello! What is your name?')
name = input()

print('Well,' ,name+',','I am thinking of a number between 1 and 20.')

for i in range(1, 21):
    print('Take a guess.')
    my_num = random.randint(1, 20)

    x = int(input())

    if my_num == x:
        print('Good job,',name + '!','You guessed my number in', i, 'guesses!')
        break
        
    else:
        print('Your guess is too low.')
