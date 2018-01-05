from collections import Counter

def scramble(s1,s2):
    cnt = Counter(s1)
    cnt.subtract(Counter(s2))
    return (all(e >= 0 for e in cnt.values()))

print(scramble('rkqodlw','world'),True)
print(scramble('cedewaraaossoqqyt','codewars'),True)
print(scramble('katas','steak'),False)
print(scramble('scriptjava','javascript'),True)
print(scramble('scriptingjava','javascript'),True)
