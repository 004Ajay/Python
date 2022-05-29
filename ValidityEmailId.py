# PYTHON PROGRAM TO CHECK THE VALIDITY OF AN EMAIL BY VERIFYING ITS FORMAT

first_half = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ0123456789'
middle_half = 'gmail, hotmail, yahoo, icloud, github, sjcet, outlook'
second_half = 'com, in, ac, ac.in, net'

email = input("Enter email: ") # email: ajaytshaju@gmail.com

part_one = email.split('@') # now email splitted into 'ajaytshaju', 'gmail.com'
part_two = part_one[1].split('.') # now 'gmail.com' becomes 'gmail', 'com'


for i in part_one[0]: #checking first half i.e 'ajaytshaju'
    if i not in first_half:
        print("Invalid Email")
        exit()

for j in part_two[0]: #checking middle half of 'gmail.com' which is 'gmail'
    if j not in middle_half:
        print("Invalid Email")
        exit()

for k in part_two[1]: #checking second half of 'gmail.com' which is 'com'
    if k not in second_half:
        print("Invalid Email")
        exit()

print("Valid Email")  #if it passes every levels of checking