# takes ~20 seconds

def Collatz(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        length += 1
    return length

maxlength = 1
n = 1
for i in range(1, 1000000):
    length = Collatz(i)
    if length > maxlength:
        maxlength = length
        n = i

print(maxlength)
print(n)