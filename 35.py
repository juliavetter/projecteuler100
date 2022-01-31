from mylib.factors import prime

# ex 123 -> [123, 231, 312]
def rotations(n : int):
    arr = []
    s = str(n)
    for i in range(len(s)):
        arr.append(s)
        s = s[-1:] + s[:-1] # put last char in front
    return arr

N = 1000000
primes = set()
for i in range(N):
    if prime(i):
        primes.add(i)



circ = set()
for p in primes:
    r = rotations(p)
    c = True
    for i in r:
        if not int(i) in primes:
            c = False
    if c:
        circ.add(i)

print(len(primes))
print(len(circ))
print(circ)