def snail(array):
    result = array[0]
    result += [a[-1] for a in array[1:]]
    result += reversed(array[-1][0:-1])
    result += [a[0] for a in reversed(array[1:-1])]
    for l in range(1, (len(array)+1)//2):
        result += array[l][l:-1*l]
        result += [a[-1*l-1] for a in array[l+1:-1*l]]
        result += reversed(array[-1*l-1][l:-1*l-1])
        result += [a[l] for a in reversed(array[l+1:-1*l-1])]
    return result

array = [[1,2],[4,3]]
print(snail(array))

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array), expected)


array = [[ 1, 2, 3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10, 9, 8,7]]
expected = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(snail(array), expected)
