import numpy as np

def palindrome(n):
    s = str(n)
    return s == s[::-1]

N = 1000000

palindromes = []

for i in range(N):
    if palindrome(np.base_repr(i, base=2)) and palindrome(np.base_repr(i, base=10)):
        palindromes.append(i)

print(sum(palindromes))