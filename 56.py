def digit_sum(n: int) -> int:
    total = 0
    for c in str(n):
        total += int(c)
    return total

maxa = 0
maxb = 0
maxsum = 0
for a in range(100):
    for b in range(100):
        t = digit_sum(a ** b)
        if t > maxsum:
            maxsum = t
            maxa = a
            maxb = b
print(maxa,maxb,maxsum)