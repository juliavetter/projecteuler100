test = [[21, 22, 23, 24, 25],
        [20, 7, 8, 9, 10],
        [19, 6, 1, 2, 11],
        [18, 5, 4, 3, 12],
        [17, 16, 15, 14, 13]]

def sum_diag(arr : list):
    sum = 0
    for i in range(len(arr)):
        j = len(arr) - i - 1
        sum += arr[i][i]
        sum += arr[i][j]
    mid = len(arr) // 2
    sum -= arr[mid][mid]
    return sum

# "turn right" if possible (if there is a 0 in the direction)
def dirQ(arr, dir, x, y):
    if   dir == "R":
        try:
            return arr[y+1][x] == 0
        except IndexError:
            pass
    elif dir == "D":
        try:
            return arr[y][x-1] == 0
        except IndexError:
            pass
    elif dir == "L":
        try:
            return arr[y-1][x] == 0
        except IndexError:
            pass
    elif dir == "U":
        try:
            return arr[y][x+1] == 0
        except IndexError:
            pass
    else:
        raise Exception("dirQ direction not found:", dir)
        return False

def next_dir(dir):
    if dir == "R":
        return "D"
    if dir == "D":
        return "L"
    if dir == "L":
        return "U"
    if dir == "U":
        return "R"

def spiral(n : int):
    arr = [0]*n
    for i in range(n):
        arr[i] = [0]*n
    x = len(arr) // 2
    y = len(arr) // 2
    dir = "R"

    # initialize middle cell before loop
    arr[y][x] = 1
    x += 1

    # loop, spiraling outwards
    for i in range(2, n * n + 1):
        arr[y][x] = i

        # determine if a direction change is in order
        if dirQ(arr, dir, x, y):
            dir = next_dir(dir)

        # proceed in current direction
        if   dir == "R":
            x += 1
        elif dir == "D":
            y += 1
        elif dir == "L":
            x -= 1
        elif dir == "U":
            y -= 1
    return arr

spiral(5)

N = 1001
print(sum_diag(spiral(1001)))