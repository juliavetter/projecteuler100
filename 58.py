from mylib.factors import prime

diags = [1,1,1,1]
n = 0

primes = 0
total = 1 # include center 1, which is never prime and not in any diagonal
while True:
    # expand the square
    for i in range(len(diags)):
        # magic formula to get next number in the diagonal
        diags[i] += 8*n + 2*(i+1)
    n += 1

    # get the number of primes in the diagonals
    for diag in diags:
        total += 1
        if prime(diag):
            primes += 1
    
    # repeat until the ratio of primes along all diagonals is < 10%
    ratio = primes / total
    if ratio <= 0.1:
        break

# print side length
print(n * 2 + 1)