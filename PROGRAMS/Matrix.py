a,b=input().split()
a,b=int(a),int(b)
c=1
for i in range(1,a+1):
  for j in range(1,b+1):
    if j!=b:
      print(c,"",end="")
    else:
      print(c,end="")
    c+=1
  if i!=a:
    print("")
  else:
    print("",end="")

   