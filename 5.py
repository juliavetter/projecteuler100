n = 0
l = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # all lower numbers are divisible by these higher numbers
increment = 2*3*5*7*11*13*17*19 # result will have to be divisible by these prime factors
i = 2*3*5*7*11*13*17*19
while True:
    divisible = True
    for j in l:
        if i % j != 0:
            divisible = False
            break
    if divisible:
        n = i
        break
    i += increment

print(n)