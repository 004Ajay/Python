# Simple Program to guess a number

import random
def guess(num):
    random_num = random.randint(1, num)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a num b\w 1 & {num}: '))
        if guess < random_num:
            print("Guess is too low")
        elif guess > random_num:
            print("Guess is too high")
    print(f'Congrats...You correctly guessed {random_num}')        

while True:
    inp_num = int(input("Enter a num(limit): "))
    guess(inp_num)
    if input("Again? y/n: ") != 'y':
        print('See you again, exited.')
        break