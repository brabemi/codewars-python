# https://www.codewars.com/kata/is-my-friend-cheating
import math

def removNb(n):
    retval = []
    overall_sum = n*(n+1)//2
    limit = math.ceil(math.sqrt(overall_sum))
    for a in range(1, limit):
        b = (overall_sum - a) // (a + 1)
        if b < n and (a * b) == (overall_sum - a - b):
            retval.append((a, b))
            retval.append((b, a))
    return sorted(retval)

print((removNb(100), []))
print((removNb(26), [(15, 21), (21, 15)]))
