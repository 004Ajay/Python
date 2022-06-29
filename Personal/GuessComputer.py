import random

def guess(limit, SecretNum):
    guess = random.randint(1, limit)
    steps = 0
    while guess != SecretNum:
        steps += 1
        guess = random.randint(1, limit)
        if guess < SecretNum:
            print(f"{guess} is too low")
        elif guess > SecretNum:
            print(f"{guess} is too high")
    print(f'Computer correctly guessed, {SecretNum}\nNumber of steps: {steps-1}') # steps - 1 for omitting the false run of loop


while True:
    LimitNum = int(input("Enter a limit number: "))
    UserSecretNum = int(input(f"Enter a secret number between 1 & {LimitNum}: "))
    inp_num = random.randint(1, LimitNum)
    guess(LimitNum, UserSecretNum)
    if input("Again? y/n: ") != 'y':
        print('See you again, exited.')
        break    