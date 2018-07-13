"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
palindromes = []
def isPal(product):
    digits = len(product)
    if digits % 2 != 0:
        return False
    if digits == 2 and product[0] == product[1]:
        return True
    if product[0] == product[-1]:
        return isPal(product[1:-1])


def getProducts(n):
    digits = str(9) * n
    for x in range(int(digits),0,-1):
        for y in range (int(digits),0,-1):
            product = str(x*y)
            if isPal(product):
                palindromes.append(int(product))
    return max(palindromes)

print(getProducts(3))