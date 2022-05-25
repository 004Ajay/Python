name=list(input())
name2=list(input())
a=""
b=""
for i in name:
  if i.isupper():
    a+=i.lower()
  elif i.islower():
    a+=i
for i in name2:
  if i.isupper():
    b+=i.lower()
  elif i.islower():
    b+=i  
if sorted(a)==sorted(b):
  print("Yes",end="")
else: 
  print("No",end="")