# super slow O(n^(5/2)) implementation
# takes ~5 minutes to run, good enough for me :)
# in fact it doesn't work :(

import math

def factors(n):
    factors = []
    for i in range(2, math.ceil(math.sqrt(n))):
        t = n / i
        if t == int(t):
            factors.append(i)
    for i in range(len(factors)):
        factors.append(n // factors[i])
    factors.append(1)
    factors.append(n)
    return factors

def amicable_pair(a, b):
    return sum(factors(a)) == sum(factors(b))

def amicable(n, max):
    for i in range(1, max):
        if n == i: # n can't be amicable with itself
            continue
        if amicable_pair(n, i):
            return True
    return False

mysum = 0
for i in range(10000):
    if i % 100 == 0:
        print(i)
    if amicable(i, 10000):
        mysum += i
print(mysum)