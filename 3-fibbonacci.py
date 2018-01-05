def my_matrix_multiply(a, b):
    m0000 = a[0][0] * b[0][0]
    # m0101 = m0110 = m1001 = m1010 = a[0][1] * b[1][0]
    m0110 = m1001 = a[0][1] * b[1][0]
    # m0001 = m0010 = a[0][0] * b[0][1]
    m0001 = a[0][0] * b[0][1]
    # m0111 = m1011 = a[0][1] * b[1][1]
    m0111 = a[0][1] * b[1][1]
    m1111 = a[1][1]*b[1][1]
    return [
        [m0000 + m0110, m0001 + m0111],
        # [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        [m0001 + m0111, m1001 + m1111]
    ]

def fib(n):
    q = 1
    if n == 0:
        return 0
    if n < 0:
        n = -1*n
        if n % 2 == 0:
            q = -1
    matrix = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    for c in '{:b}'.format(n-1)[::-1]:
        if c == '1':
            result = my_matrix_multiply(result, matrix)
        matrix = my_matrix_multiply(matrix, matrix)
    return q * result[0][0]


print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(17))
# print(fib(1000000))
print(fib(10))
print(fib(-10))
