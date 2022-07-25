# Anagrams: A meaningful word made by rearranging another word

word1=input("Enter a word: ").lower()
word2=input("Enter rearranged word: ").lower()
print(f"{word1} & {word2} are anagrams") if sorted(word1)==sorted(word2) else print(f"{word1} & {word2} are not anagrams")