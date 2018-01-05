BRACKETS = {'(': ')', '[': ']', '{': '}'}

def validBraces(string):
    stack = []
    for c in string:
        if c in '([{':
            stack.append(BRACKETS[c])
        elif not stack or c != stack.pop():
            return False
    return not stack

print(validBraces( "()" ), True);
print(validBraces( "[(])" ), False);
print(validBraces( "[()" ), False);
