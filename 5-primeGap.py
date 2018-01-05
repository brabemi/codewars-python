def prime(n, primes):
    '''
    Ta lenost, lepší udělat síto které najde prvočísla měnší než sqrt_n, pak skok a prostřílím rozsah (m, n)
    '''
    for prime in primes:
        if n % prime == 0:
            return False
    return True

def gap(g, m, n):
    sqrt_n = int(n**0.5) + 1
    primes = [True] * (sqrt_n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(sqrt_n**0.5) + 1):
        if primes[i]:
            for j in range(2*i, sqrt_n+1, i):
                primes[j] = False
    primes_tmp = [i for i in range(sqrt_n+1) if primes[i]]

    tmp_m = m if m%2 == 1 else m+1
    while tmp_m < n and not prime(tmp_m, primes_tmp):
        tmp_m += 2
    last = tmp_m
    for i in range(tmp_m, n+1, 2):
        if prime(i, primes_tmp):
            if i - last == g:
                return [last, i]
            last = i
    return None
    # your code

# gap(10,10,12)


print(gap(2, 100, 110)) # [101, 103]
print(gap(4, 100, 110)) # [103, 107]
print(gap(6, 100, 110)) # None
print(gap(8, 300, 400)) # [359, 367]
print(gap(10, 300, 400)) # [337, 347]
print(gap(2, 846160, 946160))  # [337, 347]
print(gap(2, 10000000, 20000000))  # [10000139, 10000141]
