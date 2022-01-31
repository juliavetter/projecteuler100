triangle = []
for i in range(1, 30):
    triangle.append(i * (i + 1) // 2)

words = open("42_words.txt").readline().replace("\"","").split(",")
# now words is ["a", "ability",...]

triangle_words = 0

for word in words:
    total = 0
    for char in word:
        total += ord(char) - ord('A') + 1
    if triangle[len(triangle) - 1] < total:
        raise IndexError()
    if triangle.__contains__(total):
        triangle_words += 1

print(triangle_words)