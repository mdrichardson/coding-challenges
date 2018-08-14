"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""
x = 1000
result = str(2 ** x)
total = 0
for n in result:
    total += int(n)

print(total)
