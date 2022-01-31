def palindrome(n: int):
    s = str(n)
    return s == s[::-1]