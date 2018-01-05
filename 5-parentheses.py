def valid_parentheses(string):
    cnt = 0
    for c in string:
        if c == '(':
            cnt += 1
            continue
        if c == ')':
            if cnt < 1:
                return False
            cnt -= 1
    return cnt == 0

print(valid_parentheses("  ("),False)
print(valid_parentheses(")test"),False)
print(valid_parentheses(""),True)
print(valid_parentheses("hi())("),False)
print(valid_parentheses("hi(hi)()"),True)
