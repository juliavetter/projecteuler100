# unfinished

s1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
s2 = "eleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
s3 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

sum = 0
# 1-9
for w in s1:
    sum += len(w)
sum9 = sum
# 10
sum += 3
# 11-19
sum += len(s2)
# 21-99
for tens in s3:
    # 30, 40...
    sum += len(tens)
    # 21-29, 31-39, 41-49...
    for ones in s1:
        sum += len(tens) + len(ones)
print("sum99 = ", sum)

sum99 = sum

# 100, 200, 300...
sum += len("hundred") * 9 + sum9

#101-199, 201-299...
for hundreds in s1:
    sum += 99 * (len(hundreds) + len("hundredand")) + sum99

#1000
sum += len("onethousand")

print(sum)