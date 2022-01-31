import math

N = 1000
maxp = 0
maxsols = 0

for p in range(12, N): #smallest right triangle is (3,4,5); p=3+4+5=12
    # display progress
    if p % 100 == 0:
        print(p)
    
    # find solutions for given perimeter
    sols = 0
    for a in range(1, p-1):
        for b in range(a, p-a):
            c = math.sqrt(a**2 + b**2)
            if not c.is_integer():
                continue
            if a + b + c == p:
                sols += 1

    # update max solutions
    if sols > maxsols:
        maxp = p
        maxsols = sols

print(maxp, maxsols)