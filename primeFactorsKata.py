def primeFactors(number):
    copy = int(number)
    primes = []
    while copy != 1:
        for num in range (2, int(number) +1):
            while copy % num == 0:
                copy = copy // num
                primes.append(num)
    return primes

    raise NotImplementedError