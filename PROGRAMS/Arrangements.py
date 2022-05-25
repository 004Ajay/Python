def factorial(n):
   fact = 1
   for i in range(1,n+1):
       fact = fact*i
   return fact
 
l = list(map(int,input().split()))
zeros_count = l.count(0)
ones_count = l.count(1)
num_arrangements = factorial(len(l))//(factorial(zeros_count)*factorial(ones_count))
print(num_arrangements, end='')