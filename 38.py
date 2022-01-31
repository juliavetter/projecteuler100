# returns true iff n is 9 digits long and contains each digit 1-9
def pandigital(n: int):
    s = str(n)
    if len(s) != 9:
        return False
    for i in range(1,10):
        if s.find(str(i)) == -1:
            return False
    return True

largest = 0
for i in range(0, 10000): #max range is arbitrary but gives the right answer
    for n in range(2,10):
        s = ""
        for j in range(1, n + 1):
            s = s + str(i * j)
        if pandigital(int(s)) and int(s) > largest:
            largest = int(s)

print(largest)