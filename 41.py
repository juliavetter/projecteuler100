from mylib.int import pandigitals
from mylib.factors import prime

largest_prime = 0


N = 10
for n in range(2, N): # a 1-digit pandigital would just be 1
    for i in pandigitals(n):
        if i > largest_prime and prime(i):
            largest_prime = i

print(largest_prime)