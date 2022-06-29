import random

def computer():
    def ComputerGuess(limit, SecretNum):
        CompGuess = random.randint(1, limit)
        while CompGuess != SecretNum:
            CompGuess = random.randint(1, limit)
            if CompGuess < SecretNum:
                print(f"{CompGuess} is too low")
            elif CompGuess > SecretNum:
                print(f"{CompGuess} is too high")
        print(f'Computer correctly guessed, {SecretNum}')

    while True:
        LimitNum = int(input("Enter a limit number: "))
        UserSecretNum = int(input(f"Enter a secret number between 1 & {LimitNum}: "))
        ComputerGuess(LimitNum, UserSecretNum)
        if input("Again? y/n: ") != 'y':
            print('See you again, exited.')
            break    

def human():
    def HumanGuess(num):
        HumGuess = random.randint(1, num)
        guess = 0
        while guess != HumGuess:
            guess = int(input(f'Guess a num b\w 1 & {num}: '))
            if guess < HumGuess:
                print("Guess is too low")
            elif guess > HumGuess:
                print("Guess is too high")
        print(f'Congrats...You correctly guessed {HumGuess}')        

    while True:
        inp_num = int(input("Enter a num(limit): "))
        HumanGuess(inp_num)
        if input("Again? y/n: ") != 'y':
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
    if input("All Again? y/n: ") != 'y':
        print('See you again, exited.')
        break                