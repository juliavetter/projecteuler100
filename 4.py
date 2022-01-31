def palindrome(n):
    s = str(n)
    return s == s[::-1]

palindromes = []

for i in range(1000):
    for j in range(1000):
        n = i * j
        if palindrome(n):
            palindromes.append(n)

print(max(palindromes))