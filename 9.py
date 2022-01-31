for c in range(1000):
    for b in range(c):
        for a in range(b):
            if a * a + b * b == c * c and a + b + c == 1000:
                print(a*b*c)
                exit()