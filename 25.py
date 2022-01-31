a = 1
b = 1
count = 1
while len(str(a)) < 1000:
    t = a + b
    a = b
    b = t
    count += 1
print(count)