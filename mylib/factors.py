import math

# returns a list of factors of n, including 1 and n


def factors(n: int):
    factors = [1]
    for i in range(2, math.ceil(math.sqrt(n))):
        t = n / i
        if t.is_integer():
            factors.append(i)
    for i in range(len(factors)):
        factors.append(n // factors[i])
    if math.sqrt(n).is_integer():
        factors.append(math.sqrt(n))
    return factors

# returns true iff n is prime
def prime(n: int):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True