# awful. takes ~30 seconds to run. gets the right answer

import numpy
from sympy.utilities.iterables import multiset_permutations

longest = 0
max = "0000"

def buildstr(nums: list, lops: list, sparen: str):
    l = lops.copy()
    n = nums.copy()
    n.reverse() # abcd -> dcba so we can pop the parms to get a, b, c, d
    s = ''
    for c in sparen:
        if c == '(':
            s += '('
        if c == ')':
            s += ')'
        if c == '.':
            s += l.pop()
        if c == '0':
            s += str(n.pop())
    return s

# s is some string like 'a + (b * c)'. Evaluate it left to right, obeying parentheses
def evalstr(s: str):
    try:
        return eval(s)
    except ZeroDivisionError:
        return -1
    except TypeError:
        print(s)
        exit()

def get_possibilities(a, b, c, d):
    # let a number in {0..64} correspond to some string '+++' where + = 0, - = 1, * = 2, / = 3, in base 4
    S = []
    ops = {0:'+', 1:'-', 2:'*', 3:'/'}
    # 11 possibilities of the arrangement of parentheses
    # all possibilities are considered, so the resulting string calculates left to right, obeying parentheses first
    parensops = ['0.0.0.0','(0.0).0.0','0.(0.0).0','0.0.(0.0)','(0.0.0).0','0.(0.0.0)','(0.0).(0.0)','((0.0).0).0','(0.(0.0)).0','0.((0.0).0)','0.(0.(0.0))']
    # i is in base 4. 4^3 = 256 possibilities
    for i in range(4 ** 3):
        lops = []
        for j in range(3):
            # take the jth digit of i
            t = (i // (4 ** j)) % 4
            lops.append(ops[t])
        # within this, the operation may be changed by the addition of parentheses
        for permutation in multiset_permutations([a,b,c,d]):
            for sparen in parensops:
                s = buildstr(permutation,lops,sparen)
                S.append(evalstr(s))

    # remove duplicates (sorts as byproduct)
    S = numpy.unique(S)
    # remove negatives and non-integers
    T = []
    for s in S:
        if s.is_integer() and s > 0:
            T.append(s)
    return T
        
def get_consecutive(L):
    L.sort()
    t = 1
    for l in L:
        if l != t:
            break
        t += 1
    return t - 1

for a in range(1, 7):
    print("a =",a)
    for b in range(a + 1, 8):
        print("b =",b)
        for c in range(b + 1, 9):
            for d in range(c + 1, 10):
                p = get_possibilities(a, b, c, d)
                t = get_consecutive(p)
                if t > longest:
                    longest = t
                    max = str(a) + str(b) + str(c) + str(d)

print("longest set:", longest, "max:", max)