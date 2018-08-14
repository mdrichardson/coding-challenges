"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
from decimal import *

digits = 2000
best = 0, 1

getcontext().prec = digits
for d in range(3, 1000):
    n = str(Decimal(1) / Decimal(d))[2:]
    if len(n) >= digits - 2:
        print(d, n)
        for index, c in enumerate(n[:10]):
            i = index
            test = c
            while test in n[i:] and test != n[i + 1:i + len(test) + 1]:
                test += (n[i + 1])
                i += 1
            if len(test) > best[1]:
                best = d, len(test)






print(best)