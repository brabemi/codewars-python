def append_helper(result, first, last):
    if last - first > 1:
        result.append('{}-{}'.format(first, last))
    else:
        result.append('{}'.format(first))
        if last != first:
            result.append('{}'.format(last))

def solution(args):
    if len(args) <= 1:
        return ''.join(args)
    first, last = args[0], args[0]
    result = []
    for e in args[1:]:
        if e - last == 1:
            last = e
        else:
            append_helper(result, first, last)
            first, last = e, e
    append_helper(result, first, last)
    return ','.join(result)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]) == '-6,-3-1,3-5,7-11,14,15,17-20')
print(solution([-3,-2,-1,2,10,15,16,18,19,20]) == '-3--1,2,10,15,16,18-20')
