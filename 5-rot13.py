def rot13_char(base_char, char):
    return chr((ord(char) - ord(base_char) + 13) % 26 + ord(base_char))

def rot13_helper(c):
    if c >= 'a' and c <= 'z':
        return rot13_char('a', c)
    if c >= 'A' and c <= 'Z':
        return rot13_char('A', c)
    return c

def rot13(message):
    return ''.join(map(rot13_helper, message))

print(rot13("EBG13 rknzcyr.") == "ROT13 example.")
print(rot13("This is my first ROT13 excercise!") == "Guvf vf zl svefg EBG13 rkprepvfr!")

