"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import sqrt

x = 1000

for c in range(1, x):
    for b in range(1, c):
        for a in range(1, int(sqrt(c**2-b**2))+1):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print(a,b,c)
                print(a*b*c)
                raise StopIteration('Answer Found')