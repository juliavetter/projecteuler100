def digits(n: int) -> int:
    return len(str(n))

count = 0

numer = 3
denom = 2
for i in range(1000):
    if digits(numer) > digits(denom):
        count += 1
    # seems hacky, but this actually works!!
    d = numer + denom
    n = numer + 2 * denom
    denom = d
    numer = n
print(count)