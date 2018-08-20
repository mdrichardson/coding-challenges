# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# My notes:
#   Seems like there's a good recursive solution
#   Keep a total # of ways
#   total_ways += climbStairs(n-1) for taking 1 stair
#   total_ways += climbStairs(n-2) for taking 2 stairs
#   If n == 1, return 1
#   Then return the total of both at the end?
#   Ah...this is just fibonacci
#       Let's see if we can add some memoization with a hash table

tests = [3, 5]

exists = {1: 1, 2: 2}


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n not in exists:
        exists[n] = climbStairs(n-1) + climbStairs(n-2)
    return exists[n]

for t in tests:
    print(climbStairs(t))