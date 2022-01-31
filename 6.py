N = 100
sum1 = 0
sum2 = 0

for i in range(N):
    sum1 += (i + 1) * (i + 1)

for i in range(N):
    sum2 += i + 1
sum2 *= sum2

print(sum2 - sum1)