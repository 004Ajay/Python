"""
** IMPORTANT NOTICE **

Run this code at your own risk.

This is a heavy & very inefficient code which iterates upto 
1 Lakh times to check whether the list is sorted or not.

If you're lucky then this 'Shuffling Sort' can show result 
in less than 10 steps, else a Lakh times. Chance of system crash is high.

Change the value of line -- to a value that your computer can handle.

"""
import random

while True:
    steps = 0
    lst = [1,5,3,2,4] # input your own list
    new_lst = []

    while new_lst != sorted(lst):
        srt_lst = random.shuffle(lst)
        print(lst, end=" ")
        steps += 1
        if steps >= 100000 or new_lst == sorted(lst): # change the value after '>='
            new_lst.append(srt_lst)
            print(f"\nOriginal list: {lst}\nSorted list: {new_lst}\nNumber of steps: {steps}")
            break
    if new_lst != sorted(lst):
        print("Failed after 100000 shuffling")
    if input("Do you want to continue?") == 'n' or 'N':
        break   