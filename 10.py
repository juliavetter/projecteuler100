import math

def prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        t = n / i
        if t == int(t):
            return False
    return True

N = 2000000
sum = 0
for i in range(N):
    if i % 100000 == 0:
        print(i)
    if prime(i):
        sum += i
print(sum)