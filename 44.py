# scuffed, but I guess it works. takes ~15 seconds

from bisect import bisect_left

def contains(a: list, x: int):
    'return true iff a contains x. a must be sorted'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False


N = 4000

pent = []
for i in range(1, N):
    pent.append(i*(3*i - 1) // 2)

D = 1_000_000_000
for j in pent:
    for k in pent:
        if j == k:
            continue
        if contains(pent, j + k) and contains(pent, abs(j - k)):
            D = min(D, abs(j - k))

print(D)