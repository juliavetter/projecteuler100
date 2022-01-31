from mylib.int import pandigitals

# helper function to increase clarity on line 10
def d(s: str, n: int):
    return int(s) % n == 0

total = 0
for i in pandigitals(9, 0):
    s = str(i)
    if d(s[1:4], 2) and d(s[2:5], 3) and d(s[3:6], 5) and d(s[4:7], 7) and d(s[5:8], 11) and d(s[6:9], 13) and d(s[7:10], 17):
        total += int(s)

print(total)