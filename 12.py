# takes ~15 seconds

import math

def factors(n):
    factors = []
    for i in range(2, math.ceil(math.sqrt(n))):
        t = n / i
        if t == int(t):
            factors.append(i)
    for i in range(len(factors)):
        factors.append(n // factors[i])
    return factors

triangle = 1
i = 2
while len(factors(triangle)) <= 500:

    triangle += i
    i += 1

print(triangle)