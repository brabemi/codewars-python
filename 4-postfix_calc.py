def calc(expr):
    # TODO: Your awesome code here
    if not expr:
        return 0
    parts = expr.split()
    stack = []
    for part in parts:
        if part in ['*', '/', '+', '-']:
            b = stack.pop()
            a = stack.pop()
            if part == '+':
                a += b
            elif part == '-':
                a -= b
            elif part == '*':
                a *= b
            elif part == '/':
                a /= b
            stack.append(a)
        else:
            stack.append(float(part))
    return stack.pop()


print(calc(""), 0, "Should work with empty string")
print(calc("1 2 3"), 3, "Should parse numbers")
print(calc("1 2 3.5"), 3.5, "Should parse float numbers")
print(calc("1 3 +"), 4, "Should support addition")
print(calc("1 3 *"), 3, "Should support multiplication")
print(calc("1 3 -"), -2, "Should support subtraction")
print(calc("4 2 /"), 2, "Should support division")
