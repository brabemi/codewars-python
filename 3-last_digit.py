sequences = {
    1: [1]*4,
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6]*2,
    5: [5]*4,
    6: [6]*4,
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]*2,
    0: [0]*4,
}

sequences = {n: [(n**k)%10 for k in range(1,5)] for n in range(10)}

def last_digit(lst):
    print(lst)
    acc = 1
    for n in reversed(lst[1:]):
        print(n, acc)
        if n > 1 and acc>4:
            acc = 4 + ((n%4)**(acc))%4
        else:
            acc = n**acc
        print(n, acc)
    return sequences[lst[0]%10][(acc%4)-1] if lst and acc else 1


test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
]

print(last_digit([2,3,2,1]), last_digit([2,9]))
print(last_digit([2,3,3]), last_digit([2,27]))
print(last_digit([3,2,3]), last_digit([3,8]))
print(last_digit([3,2,5]), last_digit([3,32]))
print(last_digit([3,3,2]), last_digit([3,9]))
print(last_digit([7,6,21]), last_digit([7,4]))
print(last_digit([937640, 767456, 981242]),0)
print(last_digit([0, 0]),0)


for test_input, test_output in test_data:
    print(last_digit(test_input), test_output)

# for i in range(1, 4):
    # print([(i**n)%4 for n in range(1, 21)])
