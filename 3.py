"""
The prime primes of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt

x = 600851475143
primes = []

for n in range(2, int(sqrt(x)+1)):
    if x % n == 0:
        primes.append(n)
        for z in primes[:-1]:
            if n % z == 0:
                primes.remove(n)
                break
print(max(primes))

