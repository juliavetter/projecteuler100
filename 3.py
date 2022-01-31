import math

N = 600851475143

def factors(n):
    factors = []
    for i in range(2, math.ceil(math.sqrt(n))):
        t = n / i
        if t == int(t):
            factors.append(i)
    for i in range(len(factors)):
        factors.append(n // factors[i])
    return factors

def prime(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        t = n / i
        if t == int(t):
            return False
    return True

l = factors(N)
p = []

for i in range(len(l)):
    if prime(l[i]):
        p.append(l[i])

print(max(p))