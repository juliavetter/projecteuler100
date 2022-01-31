# takes ~15 seconds

products = set()

for i in range(3000):
    for j in range(3000):
        k = i * j
        s = str(i) + str(j) + str(k)
        works = True
        if len(s) != 9:
            works = False
        for c in "123456789":
            if s.find(c) == -1:
                works = False
        if works:
            products.add(k)

print(products)
print(sum(products))