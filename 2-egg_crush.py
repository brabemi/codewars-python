import operator as op
import functools
import scipy.special

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = functools.reduce(op.mul, range(n, n-r, -1))
    denom = functools.reduce(op.mul, range(1, r+1))
    return numer//denom

def height_rec(n,m):
    if m == 0 or n == 0:
        return 0
    if m == 1:
        return 1
    if n>m:
        n = m
    return height_rec(n-1, m-1) + 1 + height_rec(n, m-1)

def height2(n,m):
    if m == 0 or n == 0:
        return 0
    if n>m:
        n = m
    a = [0]*(m+1)
    b = list(range(m+1))
    b[0] = 0
    for row in range(2,n+1):
        a[row-1] = b[row-1]
        for col in range(row,m+1-(n-row)):
            a[col] = b[col-1] + 1 + a[col-1]
        a, b = b, a

    return b[m]

def height3(n,m):
    if m == 0 or n == 0:
        return 0
    if n>m:
        n = m
    a = [0]*(n+1)
    a[n] = 1
    op = 1
    for row in range(m-1, 0, -1):
        a[0] += (row+1)*a[1]
        a[1] = a[2]
        for col in range(2, n):
            a[col] += a[col+1]
            op += a[col]
    return sum(a) + op

def height(n,m):
    if m == 0 or n == 0:
        return 0
    if n>m:
        n = m

    # bc -> https://en.wikipedia.org/wiki/Binomial_coefficient
    # bc(m, 1)
    bc = m
    cnt = bc
    for i in range(2, n+1):
        # Hockey Stick Pattern - http://ptri1.tripod.com/
        # bc(m, i) = sum(bc(x, i-1)) for x in [i-1..m-1]
        bc = bc * (m-i+1) // i
        cnt += bc
    return cnt


    # return sum(map(lambda r: ncr(m,r), range(1, n+1)))


# print(height(2,14) == height_rec(2,14))
# print(height(7,20) == height_rec(7,20))

# print(height(17,2))

print(height_rec(5,8), height(5,8))
print(height_rec(5,11), height(5,11))
print(height_rec(5,12), height(5,12))

# print(height(7,500) == 1507386560013475)
# print(height(237,500) == 431322842186730691997112653891062105065260343258332219390917925258990318721206767477889789852729810256244129132212314387344900067338552484172804802659)
# print(height(477,500) == 3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127420959866658939578436425342102468327399)
# print(height(2,10000))
# print(height(3,10000))
# print(height(2500-1000,2000))
# print(height(9500,10000))
# print(height(5,5000))
