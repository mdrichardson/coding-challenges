"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
x = 100


def fac(x):
    if x == 1:
        return x
    return x * fac(x - 1)


def fac_sum(y):
    y = str(fac(x))
    total = 0
    for d in y:
        total += int(d)
    return total

print(fac(x))
print(fac_sum(x))