import re

def is_valid_coordinates(coordinates):
    if not re.fullmatch(r'\-?\d+(\.\d+)?,\ ?\-?\d+(\.\d+)?', coordinates):
        return False
    coor = coordinates.split(',')
    if len(coor) != 2:
        return False
    lat, lot = float(coor[0]), float(coor[1])
    if (-90 <= lat <= 90) and (-180 <= lot <= 180):
        return True
    return False


valid_coordinates = [
    "-23, 25",
    "4, -3",
    "24.53525235, 23.45235",
    "04, -23.234235",
    "43.91343345, 143"
]
for v in valid_coordinates:
    print(is_valid_coordinates(v))

print()

invalid_coordinates = [
    "23.234, - 23.4234",
    "2342.43536, 34.324236",
    "N23.43345, E32.6457",
    "99.234, 12.324",
    "6.325624, 43.34345.345",
    "0, 1,2",
    "0.342q0832, 1.2324",
    "23.245, 1e1"
]
for i in invalid_coordinates:
    print(is_valid_coordinates(i))
