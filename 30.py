N = 9 ** 5 * 6

nums = []

for i in range(N):
    s = 0
    for c in str(i):
        s += int(c) ** 5
    if s == i:
        nums.append(i)
nums.remove(0)
nums.remove(1)

print(nums, sum(nums))