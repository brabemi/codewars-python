import re

def is_valid_IP(string):
    if not re.fullmatch(r'\A[1-9]\d{0,2}(\.[1-9]\d{0,2}){3}\Z', string):
        return False
    splitted = string.split('.')
    if len(splitted) != 4:
        return False
    for part in splitted:
        print(int(part))
        if not 0 <= int(part) <= 255:
            return False
    return True


print(is_valid_IP('12.255.56.1'),     True)
print(is_valid_IP(''),                False)
print(is_valid_IP('abc.def.ghi.jkl'), False)
print(is_valid_IP('123.456.789.0'),   False)
print(is_valid_IP('12.34.56'),        False)
print(is_valid_IP('12.34.56 .1'),     False)
print(is_valid_IP('12.34.56.-1'),     False)
print(is_valid_IP('123.045.067.089'), False)
