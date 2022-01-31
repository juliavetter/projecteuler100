# takes ~10 seconds

import math

def prime(n):
    if n <= 0:
        return False
    for i in range(2, math.ceil(math.sqrt(n))):
        if (n / i).is_integer():
            return False
    # special cases needed for some reason
    if n == 4:
        return False
    if math.sqrt(n).is_integer():
        return False
    return True

N = 1000
j = 2

mostprimes = 0
besta = 0
bestb = 0

for a in range(-N+1, N):
    for b in range(-N, N+1):
        n = 0
        while prime(n**2 + a * n + b):
            n += 1
        if n > mostprimes:
            mostprimes = n
            besta = a
            bestb = b

print(mostprimes, besta, bestb, besta*bestb)