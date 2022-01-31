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