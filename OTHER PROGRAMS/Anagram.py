"""
Anagrams: A meaningful word made by rearranging another word
"""

word1=list(input("Enter the word: "))
word2=list(input("Enter rearranged word: "))
a=""
b=""
for i in word1:
  if i.isupper():
    a+=i.lower()
  elif i.islower():
    a+=i
for i in word2:
  if i.isupper():
    b+=i.lower()
  elif i.islower():
    b+=i  



  print("Yes, it's an anagram") if sorted(a)==sorted(b) else print("Not an anagram")



  if sorted(a)==sorted(b):
  print("Yes",end="")
else: 
  print("No",end="")