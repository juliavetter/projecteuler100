from sympy.utilities.iterables import multiset_permutations

# returns true iff n is d digits long and contains each digit {1...d}
# d must be in {1...9}
def pandigital(n: int, d: int):
    if d > 9 or d < 1:
        return False
    s = str(n)
    if len(s) != d:
        return False
    for i in range(1, d+1):
        if s.find(str(i)) == -1:
            return False
    return True

# generates a list of all n-pandigitals
def pandigitals(end: int, start: int = 1):
    if end > 9 or start < 0 or end < start:
        return []
    s = []
    for i in range(start, end + 1):
        s.append(i)
    # now s = "1,2,...,n"
    r = []
    for i in multiset_permutations(s):
        # 0123456789 -> 123456789 is not a 0-9 pandigital
        if i[0] == 0:
            continue
        r.append(list_to_int(i))
    return r

def list_to_int(S: list):
    n = 0
    for i in S:
        n += i
        n *= 10
    return n // 10