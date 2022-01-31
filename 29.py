# thought I had to use a multiset, but it's actually really easy

N = 100
distinct = set()

for base in range(2, N + 1):
    for exp in range(2, N + 1):
        distinct.add(base ** exp)
print(len(distinct))