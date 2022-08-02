"""
Example:
Input: w o r d <each letter separated by a single space>
Output: d o r w
"""
inp = input("Enter a word separated by spaces in each alphabet: ").split(" ")
print(" ".join(sorted(inp)),end="")