def next_bigger(n):
    m = n
    acc = []
    flag_max = True
    while m > 0:
        k = m % 10
        acc.append(k)
        m //= 10
        if len(acc) >= 2 and acc[-1] < acc[-2]:
            flag_max = False
            break
    if flag_max:
        return -1
    for i in range(len(acc) - 1):
        if acc[i] > acc[-1]:
            tmp = acc[-1]
            acc[-1] = acc[i]
            acc[i] = tmp
            break
    retval = m * 10 + acc[-1]
    for e in acc[:-1]:
        retval *= 10
        retval += e

    return retval

next_bigger(2017)
next_bigger(10172)

print(next_bigger(12),21)
print(next_bigger(513),531)
print(next_bigger(2017),2071)
print(next_bigger(414),441)
print(next_bigger(144),414)
