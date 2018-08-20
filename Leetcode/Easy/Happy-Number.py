# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# My notes:
#   This is pretty clearly a good recursive problem. The issue will be making it terminate if it loops "endlessly"
#   Let's print out a bunch of tests and see how we can make it terminate
#   It looks like the sums start repeating, which makes sense. Let's add them to a dict and if the value exists, just return false


class Solution:
    def __init__(self):
        self.seen = {}

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        print(n)
        s = str(n)
        total = 0
        for i in s:
            total += int(i)**2
        if not self.seen.get(total, None):
            self.seen[total] = True
        else:
            return False
        return self.isHappy(total)