"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import sqrt

primes = []
x = 10001
test = 2
#figure out if it's prime

def isPrime(x):
    if x == 2 or x ==3:
        return True
    for n in range(2,int(sqrt(x)+1)):
        if x % n == 0:
            return False
    return True

while len(primes) < x:
    if isPrime(test):
        primes.append(test)
        test += 1
    else:
        test += 1

print('Answer: ',test - 1)


print(primes)