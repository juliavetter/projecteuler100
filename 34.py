import math

N = 100000

nums = []

for i in range(3, N):
    tot = 0
    for c in str(i):
        tot += math.factorial(int(c))
        if tot > i:
            break
    if tot == i:
        nums.append(i)

print(nums)
print(sum(nums))