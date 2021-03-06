# https://www.codewars.com/kata/coloured-triangles

import timeit

MAPPING = {
    'R': 0, 0: 'R',
    'G': 1, 1: 'G',
    'B': 2, 2: 'B',
}

def signature(n):
    retval = []
    i = 0
    while n > 0:
        n, m = divmod(n, 3)
        if m > 0:
            retval.append((i, m))
        i += 1
    return retval[::-1]

# Lucas's theorem - https://en.wikipedia.org/wiki/Lucas%27s_theorem
def triangle_rec(row, sig, pos, acc, accm):
    if pos == len(sig):
        # return (MAPPING[row[acc]] * accm) % 3
        return MAPPING[row[acc]] * accm
    retval = 0
    for i in range(sig[pos][1] + 1):
        acc_part = acc + (i * (3 ** sig[pos][0]))
        accm_part = accm
        if sig[pos][1] == 2 and i == 1:
            accm_part *= 2
        retval += triangle_rec(row, sig, pos + 1, acc_part, accm_part)
    return retval % 3

def triangle_rec_g(row, sig, pos, acc, accm):
    if pos == len(sig):
        yield (MAPPING[row[acc]] * accm) % 3
        return
        # return (MAPPING[row[acc]] * accm) % 3
    # retval = 0
    for i in range(sig[pos][1] + 1):
        acc_part = acc + (i * (3 ** sig[pos][0]))
        accm_part = accm
        if sig[pos][1] == 2 and i == 1:
            accm_part *= 2
        # retval += triangle_rec_g(row, sig, pos + 1, acc_part, accm_part)
        yield from triangle_rec_g(row, sig, pos + 1, acc_part, accm_part)
    # return retval % 3

def triangle(row):
    sig = signature(len(row) - 1)
    color_val = triangle_rec(row, sig, 0, 0, 1)
    if len(row) % 2 == 0:
        color_val = (-1 * color_val) % 3
    return MAPPING[color_val]

def triangle_g(row):
    sig = signature(len(row) - 1)
    color_val = sum(triangle_rec_g(row, sig, 0, 0, 1)) % 3
    if len(row) % 2 == 0:
        color_val = (-1 * color_val) % 3
    return MAPPING[color_val]

# R R G B R G B B
#  R B R G B R B
#   G G B R G G
#    G R G B G
#     B B R R
#      B G R
#       R B
#        G
# binom_coef(857868820)

long_input = 'B' * 857868

setup_normal = 'from __main__ import triangle'
setup_gen = 'from __main__ import triangle_g'

# command_normal = "print(triangle('" + long_input + "'), 'B')"
# command_gen = "print(triangle_g('" + long_input + "'), 'B')"
command_normal = "triangle('" + long_input + "')"
command_gen = "triangle_g('" + long_input + "')"

n = 2
for i in range(1,31):
    long_input = 'B' * (n ** i)
    command_normal = "triangle('" + long_input + "')"
    t = timeit.timeit(command_normal, setup=setup_normal, number=5)
    print(f'{n}^{i}: {t:.4f}s')

# print(timeit.timeit(command_gen, setup=setup_gen, number=100))

# print(triangle('B' * 8578688200), 'B')
# print(triangle('B' * 983501242), 'B')
# print(triangle('B' * 17), 'B')
# print(triangle_g('B' * 17), 'B')
# print(triangle('RR'), 'R')
# print(triangle('GG'), 'G')
# print(triangle('BB'), 'B')
# print(triangle('RRR'), 'R')
# print(triangle('GGG'), 'G')
# print(triangle('BBB'), 'B')
# print(triangle('RRGBRGBB'), 'G')
