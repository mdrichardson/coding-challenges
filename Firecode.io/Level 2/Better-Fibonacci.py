# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The next number is found by adding up the two numbers before it.
#
# Your goal is to write an optimal method - better_fibonacci that returns the nth Fibonacci number in the sequence.
# n is 0 indexed, which means that in the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., n == 0 should return 0 and n == 3 should return 2.
# Your method should exhibit a runtime complexity of O(n) and use constant O(1) space.
# With this implementation, your method should be able to compute larger sequences where n > 40.
#
#
# Examples:
#
# better_fibonacci(0) ==> 0
#
# better_fibonacci(1) ==> 1
#
# better_fibonacci(3) ==> 2

# My Notes:
#   - Needs to use O(n) time and O(1) space...store last two in variables and use those to add
#   - Not going to be recursive

test_inputs = [3, 4, 5, 6, 30, 10, 15]  # 832040, 55, 610

def better_fibonacci(n):
    # catch base cases
    if n <= 1:
        return n
    # Instantiate our variables with 0 and 1 index. We're starting at index 2
    nMinusOne = 1
    nMinusTwo = 0
    # For range loop from 1 until n
    for i in range(2, n + 1):
        # Set n-1 and n-2, appropriately
        nMinusTwo, nMinusOne = nMinusOne, nMinusOne + nMinusTwo
    return nMinusOne



for n in test_inputs:
    print(better_fibonacci(n))