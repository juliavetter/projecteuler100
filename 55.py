def reversed(n: int) -> int:
    return int(str(n)[::-1])

def palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

def lychrel(n: int) -> bool:
    MAX_ITER = 50
    for i in range(MAX_ITER):
        n += reversed(n)
        if palindrome(n):
            return False
    return True

total = 0
for i in range(10000):
    if lychrel(i):
        total += 1
print(total)