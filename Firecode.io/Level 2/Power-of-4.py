# Write a method to determine whether a given integer (zero or positive number) is a power of 4 without using the multiply or divide operator.
# If it is, return True, else return False.
#
# Examples:
# is_power_of_four(5) ==> False
#
# is_power_of_four(16) ==> True

# My Notes:
#   - O(n) is pretty easy...just calculate 4**x until we get to >= number, although that might count as multiplication
#   - Since the second digit in binary is 2^4, representing 4, we should be able to bit-shift left until we get there

test_inputs = [
    1,      # True
    2048,   # False
    12,     # False
    1024    # True
]


def is_power_of_four(number):
    # Instantiate an exponent
    x = 1
    while x < number:
        x = x << 2
    return x == number


for i in test_inputs:
    print(is_power_of_four(i))