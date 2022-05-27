# PYTHON PROGRAM TO GET NUMBERS AS TUPLES & SEPARATE EVEN & ODD NUMBERS THEN, PRINT THEM AS TUPLES

num = tuple(map(int,input("Enter numbers: ").split()))
even = []
odd = []
print("Input: ", num)
for i in range(1, len(num)+1):
    if (i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)

print("Even numbers: ", tuple(even))
print("Odd numbers: ", tuple(odd))