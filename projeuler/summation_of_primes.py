def gen_primes(n):
    primes = [2, 3, 5]
    number = 5
    while number+2 <= n:
        number += 2
        if number % 5 == 0:
            continue
        prime = True
        for p in primes:
            if p**2 > number:
                break
            if number % p == 0:
                prime = False
                break
        if prime:
            primes.append(number)
    return primes

primes = gen_primes(2000000)
print(sum(primes))