import math

def prime(n):
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        t = n / i
        if t == int(t):
            return False
    return True

N = 10001
primes = [2]
while len(primes) < N:
    n = primes[len(primes) - 1] + 1
    while not prime(n):
        n += 1
    primes.append(n)

print(primes[len(primes) - 1])