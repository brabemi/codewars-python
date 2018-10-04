def middle_permutation(string):
    string = sorted(string)
    retval = ''
    n = len(string)
    if n % 2 == 1:
        retval += string[n//2]
        string = string[:n//2] + string[n//2+1:]
        n -= 1
    retval += string[n//2-1]
    string = string[:n//2-1] + string[n//2:]
    retval += ''.join(string[::-1])
    return retval

print(middle_permutation("abc"),"bac")
print(middle_permutation("abcd"),"bdca")
print(middle_permutation("abcdx"),"cbxda")
print(middle_permutation("abcdxg"),"cxgdba")
print(middle_permutation("abcdxgz"),"dczxgba")
print(middle_permutation("abcdefghijklmnopqrst"),"dczxgba")
