def spiralize(size):
    spiral = [[0]*size for i in range(size)]

    # right, can solve size 1
    for i in range(size):
        spiral[0][i] = 1

    # down, can solve size 2
    if size >= 2:
        for i in range(size):
           spiral[i][size-1] = 1

    # left, can solve size 3
    if size >= 3:
        for i in range(size):
           spiral[size-1][i] = 1

    # up, can solve size 4
    if size >= 4:
        for i in range(2, size):
           spiral[i][0] = 1

    if size >= 5:
        # connection
        spiral[2][1] = 1

        # fill middle
        center = spiralize(size-4)
        for row in range(size-4):
            for col in range(size-4):
                spiral[row+2][col+2] = center[row][col]

    return spiral

for i in range(11):
    for part in spiralize(i):
        print(part)
    print()
