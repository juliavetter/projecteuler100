def get_score(s):
    score = 0
    for c in s:
        score += ord(c) + 1 - ord('A')
    return score

names = open("22_names.txt", "r").readline().replace("\"","").split(",")
names.sort()
total = 0
for i in range(len(names)):
    total += (i + 1) * get_score(names[i])
print(total)