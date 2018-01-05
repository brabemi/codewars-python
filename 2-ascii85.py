import base64

# def toAscii85(data):
#     return '<~' + base64.a85encode(data.encode()).decode('ASCII') + '~>'

# def fromAscii85(data):
#     return base64.a85decode(data[2:-2].encode()).decode('ASCII')

def toAscii85(data):
    return '<~' + base64.a85encode(bytes([ord(c) for c in data])).decode('ascii') + '~>'

def fromAscii85(data):
    return ''.join([ chr(c) for c in base64.a85decode(data[2:-2].encode('ascii'))])

print('test\x99'.encode('eascii'))

# print(toAscii85('easy'), '<~ARTY*~>')
# print(toAscii85('somewhat difficult'), '<~F)Po,GA(E,+Co1uAnbatCif~>')
# print(fromAscii85('<~ARTY*~>'), 'easy')
# print(fromAscii85('<~F)Po,GA(E,+Co1uAnbatCif~>'), 'somewhat difficult')
