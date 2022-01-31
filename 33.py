# return true iff a and b match at least one digit
def match_dig(a:int, b:int):
    d = str(b)
    for c in str(a):
        if d.find(c) != -1:
            return True
    return False

# return true if a is within .001 of b
def xeq(a:float, b:float):
    return abs(a - b) < 0.001

wow = []

for numerator in range(10, 100):
    for denominator in range(10, 100):
        # requirement: < 1 in value
        if numerator >= denominator:
            continue
        # useless, but doesn't hurt
        if not match_dig(numerator, denominator):
            continue
        # now see if we can "cancel" a digit from the numerator and denominator
        s1 = numerator // 10
        s2 = numerator % 10
        d1 = denominator // 10
        d2 = denominator % 10
        frac = numerator / denominator
        try:
            if   s1 == d1 != 0:
                cancel = s2 / d2
                if xeq(frac, cancel):
                    wow.append({numerator, denominator})
            elif s1 == d2 != 0:
                cancel = s2 / d1
                if xeq(frac, cancel):
                    wow.append({numerator, denominator})
            elif s2 == d1 != 0:
                cancel = s1 / d2
                if xeq(frac, cancel):
                    wow.append({numerator, denominator})
            elif s2 == d2 != 0:
                cancel = s1 / d1
                if xeq(frac, cancel):
                    wow.append({numerator, denominator})
        except ZeroDivisionError:
            pass

print(wow)