# Guessing program combination for computer & human

import random

def computer():
    def ComputerGuess(limit, SecretNum):
        CompGuess = random.randint(1, limit) # computer guessing a random num
        steps = 0
        while CompGuess != SecretNum:
            steps += 1 # incrementing step count
            CompGuess = random.randint(1, limit)
            if CompGuess < SecretNum:
                print(f"{CompGuess} is too low")
            elif CompGuess > SecretNum:
                print(f"{CompGuess} is too high")
        print(f'Computer correctly guessed, {SecretNum}\nNumber of steps: {steps-1}') # steps - 1 for omitting the false run of loop

    while True:
        LimitNum = int(input("Enter a limit number: ")) # Human entering limit
        UserSecretNum = int(input(f"Enter a secret number between 1 & {LimitNum}: ")) # Human entering secret num to be guessed by computer
        ComputerGuess(LimitNum, UserSecretNum)
        if input("Again? y/n: ") != 'y': # For breaking while loop
            print('See you again, exited.')
            break    

def human():
    def HumanGuess(num):
        HumGuess = random.randint(1, num) # computer takes a random number for human to guess
        guess = steps = 0
        while guess != HumGuess:
            steps += 1 # incrementing step count
            guess = int(input(f'Guess a num b\w 1 & {num}: ')) # getting guess number
            if guess < HumGuess:
                print("Guess is too low")
            elif guess > HumGuess:
                print("Guess is too high")
        print(f'Congrats...You correctly guessed {HumGuess}\nNumber of steps: {steps-1}') # steps - 1 for omitting the false iteration of loop

    while True:
        inp_num = int(input("Enter a num(limit): "))
        HumanGuess(inp_num) 
        if input("Again? y/n: ") != 'y': # For breaking while loop
            print('See you again, exited.')
            break

while True:
    choice = int(input("1: Guess by Computer\n2: Guess by Human\nChoice: "))
    if choice == 1:
        computer()
    elif choice == 2:
        human()
    else:
        print("Choice is out of range...")
    if input("All Again? y/n: ") != 'y': # For breaking while loop
        print('See you again, exited.')
        break                