from collections import Counter

def myPerm(cntr):
    perms = []
    for e in cntr:
        if cntr[e] > 0:
            cntr[e] -= 1
            for perm in myPerm(cntr):
                perms.append(e + perm)
            cntr[e] += 1
    return perms if perms else ['']


def permutations(string):
    cntr = Counter(string)
    return myPerm(cntr)

print(sorted(permutations('a')), ['a'])
print(sorted(permutations('ab')), ['ab', 'ba'])
print(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
