fib = [1,2]
a = 1
b = 2
# produce fibonacci sequence up to 4 million
while b < 4000000:
    t = a + b
    a = b
    b = t
    fib.append(b)
# set all odd numbers to 0 (in preparation for sum)
for i in range(len(fib)):
    if fib[i] % 2 == 1:
        fib[i] = 0
        
print(sum(fib))