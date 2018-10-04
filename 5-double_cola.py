# https://www.codewars.com/kata/double-cola

def whoIsNext(names, r):
    queue_len = len(names)
    while r > queue_len:
        r -= queue_len
        queue_len *= 2
    return names[(r-1) * len(names) // queue_len]

print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1)=="Sheldon")
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 6)=="Sheldon")
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7)=="Sheldon")
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52)=="Penny")
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951)=="Leonard")
