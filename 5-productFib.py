
def productFib(prod):
    F1 = 0
    F2 = 1
    while True:
        if F1 * F2 == prod:
            return [F1, F2, True]
        if F1 * F2 > prod:
            return [F1, F2, False]
        F2 += F1
        F1 = F2 - F1


print(productFib(4895)) # [55, 89, True]
print(productFib(5895)) # [89, 144, False]
