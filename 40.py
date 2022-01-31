N = 1000000 # just a guess (added 0s until i didn't get IndexError)

d = ""
for i in range(N):
    d += str(i)

prod = 1

vals = [1,10,100,1000,10_000,100_000,1_000_000]
for i in vals:
    prod *= int(d[i])

print(prod)