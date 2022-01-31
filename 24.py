# takes ~ 30 seconds to run

from sympy.utilities.iterables import multiset_permutations

s = range(0,10)
S = multiset_permutations(s)
T = []
for s in S:
    t = ''
    for c in s:
        t += str(c)
    T.append(t)
T.sort()
# turns out this is correct rather than T[1000000]
print(T[999999])