def height(n,m):
    if m == 0 or n == 0:
        return 0
    if n>m:
        n = m
    bc = m
    cnt = bc
    for i in range(2, n+1):
        bc = bc * (m-i+1) // i
        cnt = (cnt + (bc % 998244353)) % 998244353
    return cnt

# print(height(80000, 100000))
print(height(3000, 2**200))
