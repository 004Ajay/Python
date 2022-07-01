# Simple Program for computer to guess a number

import random

def guess(limit, SecretNum):
    guess = random.randint(1, limit) # computer guessing a random num
    steps = 0
    while guess != SecretNum:
        steps += 1 # incrementing step count
        guess = random.randint(1, limit)
        if guess < SecretNum:
            print(f"{guess} is too low")
        elif guess > SecretNum:
            print(f"{guess} is too high")
    print(f'Computer correctly guessed, {SecretNum}\nNumber of steps: {steps}') # steps - 1 for omitting the false run of loop


while True:
    LimitNum = int(input("Enter a limit number: ")) # Human entering limit
    UserSecretNum = int(input(f"Enter a secret number between 1 & {LimitNum}: ")) # Human entering secret num to be guessed by computer
    guess(LimitNum, UserSecretNum)
    if input("Again? y/n: ") != 'y': # For breaking while loop
        print('See you again, exited.')
        break    