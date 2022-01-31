# takes ~15 seconds

from mylib.factors import prime

def trunc_l(n : int):
    s = str(n)
    while len(s) > 0:
        if not prime(int(s)):
            return False
        s = s[1:]
    return True

def trunc_r(n : int):
    while n != 0:
        if not prime(n):
            return False
        n //= 10
    return True

trunc = []

# skip 2,3,5,7
i = 10
while len(trunc) < 11:
    if trunc_r(i) and trunc_l(i):
        trunc.append(i)
    i += 1

print(len(trunc))
print(trunc)
print(sum(trunc))