# https://www.codewars.com/kata/binomial-expansion/train/python

import math

def axb_extract(expr):
    expr = expr[::-1]
    parts = expr.split('+', 1)
    if len(parts) != 2:
        parts = expr.split('-', 1)
        parts[0] += '-'

    a_str = parts[1]
    a_str = a_str[1:]
    a_str = a_str[::-1]
    if a_str == '' or a_str == '-':
        a_str += '1'

    a = int(a_str)
    x = parts[1][0]
    b = int(parts[0][::-1])

    return a, x, b

def binom_coef(n):
    top = list(range(n, math.floor((n+1)/2), -1))
    bot = list(range(1, math.ceil((n+1)/2), 1))

    for i in range(1, len(top)):
        top[i] *= top[i-1]
        bot[i] *= bot[i-1]

    coef = [1]
    for i in range(len(top)):
        coef.append(top[i]//bot[i])

    coef2 = coef if n % 2 == 1 else coef[:-1]
    coef += coef2[::-1]

    return coef

def expand(expr):
    parts = expr.split('^', 1)
    exponent = int(parts[1])

    if exponent == 0:
        return '1'
    elif exponent == 1:
        return parts[0][1:-1]

    a, x, b = axb_extract(parts[0][1:-1])

    coef = binom_coef(exponent)
    # print(bc)

    qa = 1
    qb = 1
    for i in range(exponent+1):
        coef[exponent-i] *= qb
        coef[i] *= qa
        qb *= b
        qa *= a

    elements = []

    for i in range(exponent, -1, -1):
        sign = '+' if coef[i] > 0 else '-'
        elem_coef = abs(coef[i]) if abs(coef[i]) > 1 else ''
        if i > 1:
            elements.append('{}{}{}^{}'.format(sign, elem_coef, x, i))
        elif i == 1:
            elements.append('{}{}{}'.format(sign, elem_coef, x))
        else:
            elements.append('{}{}'.format(sign, elem_coef))

    if elements[0][0] == '+':
        elements[0] = elements[0][1:]

    if len(elements[-1]) == 1:
        elements[-1] += '1'

    return ''.join(elements)





print(expand("(2x+1)^0"), "1")
print(expand("(x+1)^0"), "1")
print(expand("(x+1)^1"), "x+1")
print(expand("(x+1)^2"), "x^2+2x+1")

print(expand("(x-1)^0"), "1")
print(expand("(x-1)^1"), "x-1")
print(expand("(x-1)^2"), "x^2-2x+1")

print(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
print(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
print(expand("(7x-7)^0"), "1")

print(expand("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81")
print(expand("(-2k-3)^3"), "-8k^3-36k^2-54k-27")
print(expand("(-7x-7)^0"), "1")
