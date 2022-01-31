# Takes a long time, but it works

import math

N = 28123

def factors(n):
    factors = []
    for i in range(2, math.ceil(math.sqrt(n))):
        t = n / i
        if t == int(t):
            factors.append(i)
    for i in range(len(factors)):
        factors.append(n // factors[i])
    s = math.sqrt(n)
    if int(s) == s:
        factors.append(int(s))
    factors.append(1)
    return factors

def abundant(n):
    return sum(factors(n)) > n

def get_abundants(max):
    a = []
    for i in range(2, max):
        if abundant(i):
            a.append(i)
    return a

# return true iff n cannot be written as a sum of two elements in l
def cant(n, l):
    for i in l:
        if i > n:
            break
        for j in l:
            if j > n:
                break
            if n == i + j:
                return False
    return True

abundants = get_abundants(N)
listcant = []
for i in range(N):
    if i % 100 == 0:
        print(i)
    if cant(i, abundants):
        listcant.append(i)
print(sum(listcant))