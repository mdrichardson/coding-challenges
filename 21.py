"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
x = 10000


def get_divisors(z):
    total = 0
    for n in range(1, int(z/2) + 1):
        if z % n == 0:
            total += n
    return total


def is_amicable(y):
    test = get_divisors(y)
    if get_divisors(test) == y and y != test:
        return True
    else:
        return False

amicable = []

for i in range(1, x):
    if is_amicable(i):
        amicable.append(i)

print(amicable)
print(sum(amicable))



