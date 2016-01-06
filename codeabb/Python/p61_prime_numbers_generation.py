"""
CodeAbbey, Problem 61
Coded by whoisrgj
"""

N = int(input())
numbers = list(map(int, input().split()))

def gen_primes(n):
    primes = [2]
    number = 1
    pcount = 1
    while pcount <= n:
        number += 2
        if number > 5 and number % 5 == 0:
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
            pcount += 1
    return primes

primes = gen_primes(200000)

for i in numbers:
    print(primes[i-1], end=' ')
    