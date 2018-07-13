"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when
n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the
consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces
the maximum number of primes for consecutive values of n, starting with n = 0.
"""
from math import sqrt

end_a = 1000
end_b = 1000
best = 0,0,0,0


def is_prime(x):
    if x % 2 == 0:
        return False
    try:
        for y in range(3, int(sqrt(x)) + 1, 2):
            if x % y == 0:
                return False
    except:
        return False
    return True

for a in range(-end_a, end_a + 1):
    for b in range(-end_b, end_b + 1):
        n = 0
        while is_prime(n**2 + (a * n) + b):
            n += 1
        if n > best[0]:
            best = n, a, b, a*b
        print(a,b)

print(best)