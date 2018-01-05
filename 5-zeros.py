def zeros2(n):
    acc = 5
    zeros = 0
    while n // acc > 0:
        zeros += n // acc
        acc *= 5
    return zeros

def zeros1(n):
    k = 1
    acc = 5
    while acc * 5 < n:
        acc *= 5
        k += 1
    print(n, acc, k)

def zeros(n):
    twos = 0
    fives = 0
    for i in range(5, n+1, 5):
        # while i > 0 and i % 10 == 0:
        #     twos += 1
        #     fives += 1
        #     i //= 10
        # while i > 0 and i % 2 == 0:
        #     twos += 1
        #     i //= 2
        while i > 0 and i % 5 == 0:
            fives += 1
            i //= 5
    # return fives if fives < twos else twos
    return fives



print(zeros2(12), 2)
print(zeros2(5), 1)
print(zeros2(20), 4)
print(zeros2(1000), 249)
