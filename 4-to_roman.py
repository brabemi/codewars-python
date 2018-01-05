FACTORS = [
    ['M', 1000], ['CM', 900], ['D', 500], ['CD', 400],
    ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
    ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]
]

def solution(n):
    retval = ''
    for factor in FACTORS:
        count, n = divmod(n, factor[1])
        retval += count * factor[0]
    return retval

def solution_rev(string):
    num = 0
    index = 0
    for factor in FACTORS:
        while string.startswith(factor[0], index):
            num += factor[1]
            index += len(factor[0])
    return num

# print(solution(1))
# print(solution(4))
# print(solution(5))
# print(solution(6))
# print(solution(58))

print(solution_rev(solution(1)))
print(solution_rev(solution(4)))
print(solution_rev(solution(5)))
print(solution_rev(solution(6)))
print(solution_rev(solution(58)))
