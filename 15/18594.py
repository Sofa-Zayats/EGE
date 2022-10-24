for a in range(64):
    f = True
    for m in range(64):
        for n in range(64):
            if not((2 * m + 3 * n > 43) or (m < a) or (n <= a)):
                f = False
    if f:
        print(a)
        break
