def validate(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num

def rgb_my(r, g, b):
    r = validate(r)
    g = validate(g)
    b = validate(b)
    return '{:02X}{:02X}{:02X}'.format(r, g, b)

def rgb(r, g, b):
    rnd = lambda x: max(0, min(255, x))
    return '{:02X}{:02X}{:02X}'.format(rnd(r), rnd(g), rnd(b))

print(rgb(0,0,0),"000000", "testing zero values")
print(rgb(1,2,3),"010203", "testing near zero values")
print(rgb(255,255,255), "FFFFFF", "testing max values")
print(rgb(254,253,252), "FEFDFC", "testing near max values")
print(rgb(-20,275,125), "00FF7D", "testing out of range values")
