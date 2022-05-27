# PYTHON PROGRAM TO REMOVE THE OCCURANCE OF A NUMBER IN A LIST


list = map(int, input("Enter list: ").split())
num = int(input("Enter num to remove: "))

for i in list:
    if(i != num): print(i)